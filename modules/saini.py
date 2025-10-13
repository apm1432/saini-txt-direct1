import os
import re
import time
import mmap
import datetime
import asyncio
import aiohttp
import aiofiles
import logging
import requests
import subprocess
import tempfile
import shutil
import gc
import concurrent.futures
from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message
from utils import progress_bar
import globals


# -------------------- Utilities --------------------

def cleanup_temp_files(folder=None):
    """Delete temp files in a folder. If folder=None, delete in current dir."""
    folder = Path(folder) if folder else Path(os.getcwd())
    for f in folder.iterdir():
        if f.is_file() and f.suffix.lower() in (".part", ".m4a", ".mp4.temp", ".aria2", ".jpg", ".mkv", ".webm"):
            try:
                f.unlink()
            except Exception as e:
                print(f"Failed to delete {f}: {e}")
    gc.collect()


def duration(filename):
    """Return duration of video in seconds using ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    return float(result.stdout.decode().strip())


def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0 or unit == 'PB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def time_name():
    date = datetime.date.today()
    now = datetime.datetime.now()
    current_time = now.strftime("%H%M%S")
    return f"{date} {current_time}.mp4"


# -------------------- MPD/Keys --------------------

def get_mps_and_keys(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        mpd = data.get("url") or data.get("URL") or data.get("mpd") or data.get("MPD")
        keys = data.get("keys") or data.get("KEYS") or []
        if not mpd or not keys:
            return None, None
        return mpd, keys
    except Exception as e:
        print(f"Error fetching MPD/Keys: {e}")
        return None, None


def get_mps_and_keys2(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        mpd = data.get("url") or data.get("URL") or data.get("mpd") or data.get("MPD")
        keys = data.get("keys") or data.get("KEYS") or []
        if not mpd or not keys:
            return None, None
        return mpd, keys
    except Exception as e:
        print(f"Error fetching MPD/Keys: {e}")
        return None, None

def get_mps_and_keys1(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        mpd = data.get("url") or data.get("URL") or data.get("mpd") or data.get("MPD")
        keys = data.get("keys") or data.get("KEYS") or []
        if not mpd or not keys:
            return None, None
        return mpd, keys
    except Exception as e:
        print(f"Error fetching MPD/Keys: {e}")
        return None, None

# -------------------- Video Info Parsing --------------------

def parse_vid_info(info):
    info = info.strip().split("\n")
    new_info = []
    temp = []
    for i in info:
        i = str(i)
        if "[" not in i and '---' not in i:
            i = re.sub(r" +", " ", i).strip()
            parts = i.split("|")[0].split(" ", 2)
            try:
                if "RESOLUTION" not in parts[2] and parts[2] not in temp and "audio" not in parts[2]:
                    temp.append(parts[2])
                    new_info.append((parts[0], parts[2]))
            except:
                pass
    return new_info


def vid_info(info):
    info = info.strip().split("\n")
    new_info = dict()
    temp = []
    for i in info:
        i = str(i)
        if "[" not in i and '---' not in i:
            i = re.sub(r" +", " ", i).strip()
            parts = i.split("|")[0].split(" ", 3)
            try:
                if "RESOLUTION" not in parts[2] and parts[2] not in temp and "audio" not in parts[2]:
                    temp.append(parts[2])
                    new_info[parts[2]] = parts[0]
            except:
                pass
    return new_info


# -------------------- Decryption --------------------

def decrypt_file(file_path, key):
    """Simple XOR decryption on first 28 bytes of file."""
    if not os.path.exists(file_path):
        return False
    with open(file_path, "r+b") as f:
        num_bytes = min(28, os.path.getsize(file_path))
        with mmap.mmap(f.fileno(), length=num_bytes, access=mmap.ACCESS_WRITE) as mmapped_file:
            for i in range(num_bytes):
                mmapped_file[i] ^= ord(key[i]) if i < len(key) else i
    return True


# -------------------- Video Download & Decrypt --------------------

failed_counter = 0  # Global counter for retries


async def download_video(url, cmd, name):
    """Download a video using yt-dlp into a temp folder and copy to cwd."""
    global failed_counter
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir) / name
            download_cmd = (
                f'{cmd} -R 25 --fragment-retries 25 '
                f'--external-downloader aria2c '
                f'--downloader-args "aria2c: -x 16 -j 32" '
                f'-o "{tmp_path}" "{url}"'
            )
            print(f"Running command: {download_cmd}")
            logging.info(download_cmd)

            result = subprocess.run(download_cmd, shell=True)

            if "visionias" in cmd and result.returncode != 0 and failed_counter <= 10:
                failed_counter += 1
                await asyncio.sleep(5)
                return await download_video(url, cmd, name)
            failed_counter = 0

            downloaded_file = None
            for ext in ["", ".webm", ".mkv", ".mp4", ".mp4.webm"]:
                candidate = tmp_path.with_suffix(ext)
                if candidate.exists():
                    downloaded_file = candidate
                    break

            if not downloaded_file:
                print(f"Download failed for {name}")
                return None

            # Copy to current directory
            final_file = Path(os.getcwd()) / downloaded_file.name
            shutil.copy(downloaded_file, final_file)
            gc.collect()
            return str(final_file)
    except Exception as e:
        print(f"Error during download_video: {e}")
        return None


async def download_and_decrypt_video(url, cmd, name, key):
    """Download a video and decrypt it."""
    try:
        video_path = await download_video(url, cmd, name)
        if not video_path:
            print(f"Failed to download {name}")
            return None
        if decrypt_file(video_path, key):
            print(f"File decrypted successfully: {video_path}")
            return video_path
        else:
            print(f"Decryption failed for {video_path}")
            return None
    except Exception as e:
        print(f"Error in download_and_decrypt_video: {e}")
        return None


# -------------------- Video Decrypt & Merge --------------------

async def decrypt_and_merge_video(mpd_url, keys_string, output_name, quality="720"):
    """Download, decrypt, merge video/audio with optional watermark."""
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            cmd1 = (
                f'yt-dlp -f "bv[height<={quality}]+ba/b" '
                f'-o "{tmp_path}/file.%(ext)s" '
                f'--allow-unplayable-format --no-check-certificate '
                f'--external-downloader aria2c "{mpd_url}"'
            )
            print(f"Running command: {cmd1}")
            os.system(cmd1)

            av_files = list(tmp_path.iterdir())
            video_decrypted = False
            audio_decrypted = False

            for f in av_files:
                if f.suffix == ".mp4" and not video_decrypted:
                    cmd2 = f'mp4decrypt {keys_string} --show-progress "{f}" "{tmp_path}/video.mp4"'
                    os.system(cmd2)
                    if (tmp_path / "video.mp4").exists():
                        video_decrypted = True
                    f.unlink()
                elif f.suffix == ".m4a" and not audio_decrypted:
                    cmd3 = f'mp4decrypt {keys_string} --show-progress "{f}" "{tmp_path}/audio.m4a"'
                    os.system(cmd3)
                    if (tmp_path / "audio.m4a").exists():
                        audio_decrypted = True
                    f.unlink()

            if not video_decrypted or not audio_decrypted:
                raise FileNotFoundError("Decryption failed: video or audio missing.")

            merged_file = tmp_path / f"{output_name}.mp4"
            if globals.vidwatermark != "/d":
                watermark_filter = (
                    f"drawtext=fontfile=vidwater.ttf:text='{globals.vidwatermark}':"
                    f"fontcolor=black@0.7:fontsize=h/10:x=(w-text_w)/9:y=(h-text_h)/9"
                )
                cmd4 = f'ffmpeg -i "{tmp_path}/video.mp4" -i "{tmp_path}/audio.m4a" ' \
                       f'-vf "{watermark_filter}" -c:v libx264 -preset ultrafast -crf 23 -c:a copy "{merged_file}"'
            else:
                cmd4 = f'ffmpeg -i "{tmp_path}/video.mp4" -i "{tmp_path}/audio.m4a" -c copy "{merged_file}"'
            os.system(cmd4)

            for f in ("video.mp4", "audio.m4a"):
                path_f = tmp_path / f
                if path_f.exists():
                    path_f.unlink()

            final_file = Path(os.getcwd()) / f"{output_name}.mp4"
            shutil.copy(merged_file, final_file)
            gc.collect()
            return str(final_file)
    except Exception as e:
        print(f"Error during decrypt_and_merge_video: {e}")
        raise


# -------------------- Async Run --------------------

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        print(f"[stdout]\n{stdout.decode()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode()}")
    return proc.returncode


# -------------------- Send PDF / Video --------------------

async def send_doc(bot: Client, m: Message, cc, ka, cc1, prog, count, name, channel_id):
    reply = await bot.send_message(channel_id, f"Downloading pdf:\n<pre><code>{name}</code></pre>")
    await asyncio.sleep(1)
    await bot.send_document(ka, caption=cc1)
    count += 1
    await reply.delete(True)
    await asyncio.sleep(1)
    os.remove(ka)
    await asyncio.sleep(3)


async def send_vid(bot: Client, m: Message, cc, filename, vidwatermark, thumb, name, prog, channel_id):
    try:
        thumb_file = f"{filename}.jpg"
        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:00:10 -vframes 1 "{thumb_file}"', shell=True)

        if prog:
            await prog.delete(True)
        reply1 = await bot.send_message(channel_id, f"**📩 Uploading Video 📩:-**\n<blockquote>**{name}**</blockquote>")
        reply = await m.reply_text(f"**Generate Thumbnail:**\n<blockquote>**{name}**</blockquote>")

        thumbnail = thumb_file if thumb == "/d" else thumb
        dur = int(duration(filename))
        start_time = time.time()

        try:
            await bot.send_video(
                channel_id, filename, caption=cc, supports_streaming=True,
                height=720, width=1280, thumb=thumbnail,
                duration=dur, progress=progress_bar, progress_args=(reply, start_time)
            )
        except Exception:
            await bot.send_document(
                channel_id, filename, caption=cc,
                progress=progress_bar, progress_args=(reply, start_time)
            )

        os.remove(filename)
        os.remove(thumb_file)
        await reply.delete(True)
        await reply1.delete(True)
        cleanup_temp_files()
        print("🧹 Cache and temp files cleaned successfully.")

    except Exception as e:
        print(f"Error in send_vid: {e}")
