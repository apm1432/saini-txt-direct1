import globals
from vars import CREDIT
import random
import json
import os
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, InputMediaPhoto

# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
def register_settings_handlers(bot):
    
    @bot.on_callback_query(filters.regex("setttings"))
    async def settings_button(client, callback_query):
        caption = "✨ <b>My Premium BOT Settings Panel</b> ✨"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📝 Caption Style", callback_data="caption_style_command"), InlineKeyboardButton("🖋️ File Name", callback_data="file_name_command")],
            [InlineKeyboardButton("🌅 Thumbnail", callback_data="thummbnail_command")],
            [InlineKeyboardButton("✍️ Add Credit", callback_data="add_credit_command"), InlineKeyboardButton("🔏 Set Token", callback_data="set_token_command")],
            [InlineKeyboardButton("💧 Watermark", callback_data="wattermark_command")],
            [InlineKeyboardButton("📽️ Video Quality", callback_data="quality_command"), InlineKeyboardButton("🏷️ Topic", callback_data="topic_command")],
            [InlineKeyboardButton("🔄 Reset", callback_data="resset_command")],
            [InlineKeyboardButton("⚙️ Manage APIs", callback_data="manage_apis")],
            [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main_menu")]
        ])
        await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://envs.sh/GVI.jpg",
          caption=caption
        ),
        reply_markup=keyboard
        )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("thummbnail_command"))
    async def cmd(client, callback_query):
        user_id = callback_query.from_user.id
        first_name = callback_query.from_user.first_name
        caption = f"✨ **Welcome [{first_name}](tg://user?id={user_id})\nChoose Button to set Thumbnail**"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🎥 Video", callback_data="viideo_thumbnail_command"), InlineKeyboardButton("📑 PDF", callback_data="pddf_thumbnail_command")],
            [InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]
        ])
        await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://tinypic.host/images/2025/07/14/file_00000000fc2461fbbdd6bc500cecbff8_conversation_id6874702c-9760-800e-b0bf-8e0bcf8a3833message_id964012ce-7ef5-4ad4-88e0-1c41ed240c03-1-1.jpg",
          caption=caption
        ),
        reply_markup=keyboard
        )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("wattermark_command"))
    async def cmd(client, callback_query):
        user_id = callback_query.from_user.id
        first_name = callback_query.from_user.first_name
        caption = f"✨ **Welcome [{first_name}](tg://user?id={user_id})\nChoose Button to set Watermark**"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🎥 Video", callback_data="video_wateermark_command"), InlineKeyboardButton("📑 PDF", callback_data="pdf_wateermark_command")],
            [InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]
        ])
        await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://tinypic.host/images/2025/07/14/file_00000000fc2461fbbdd6bc500cecbff8_conversation_id6874702c-9760-800e-b0bf-8e0bcf8a3833message_id964012ce-7ef5-4ad4-88e0-1c41ed240c03-1-1.jpg",
          caption=caption
        ),
        reply_markup=keyboard
        )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
  # async def cmd(client, callback_query):
   #     user_id = callback_query.from_user.id
    #    first_name = callback_query.from_user.first_name
     #   caption = f"✨ **Welcome [{first_name}](tg://user?id={user_id})\nChoose Button to set Token**"
      #  keyboard = InlineKeyboardMarkup([
       #     [InlineKeyboardButton("Classplus", callback_data="cp_token_command")],
        #    [InlineKeyboardButton("Physics Wallah", callback_data="pw_token_command"), InlineKeyboardButton("Carrerwill", callback_data="cw_token_command")],
         #   [InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]
        #])
       # await callback_query.message.edit_media(
        #InputMediaPhoto(
         # media="https://tinypic.host/images/2025/07/14/file_00000000fc2461fbbdd6bc500cecbff8_conversation_id6874702c-9760-800e-b0bf-8e0bcf8a3833message_id964012ce-7ef5-4ad4-88e0-1c41ed240c03-1-1.jpg",
          #caption=caption
        #),
        #reply_markup=keyboard
        #)
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("set_token_command"))
    async def cmd(client, callback_query):
        user_id = callback_query.from_user.id
        first_name = callback_query.from_user.first_name
        caption = f"✨ **Welcome [{first_name}](tg://user?id={user_id})\nChoose Button to set Token**"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Classplus ➕ Add", callback_data="cp_add_token_command"),
             InlineKeyboardButton("Classplus 🗑️ Delete", callback_data="cp_del_token_command")],
            [InlineKeyboardButton("Physics Wallah", callback_data="pw_token_command"),
             InlineKeyboardButton("Carrerwill", callback_data="cw_token_command")],
            [InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]
        ])
        await callback_query.message.edit_media(
        InputMediaPhoto(
            media="https://tinypic.host/images/2025/07/14/file_00000000fc2461fbbdd6bc500cecbff8_conversation_id6874702c-9760-800e-b0bf-8e0bcf8a3833message_id964012ce-7ef5-4ad4-88e0-1c41ed240c03-1-1.jpg",
            caption=caption
          ),
          reply_markup=keyboard
          ) 
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("caption_style_command"))
    async def handle_caption(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]])
        editable = await callback_query.message.edit(
            "**Caption Style 1**\n"
            "<blockquote expandable><b>[🎥]Vid Id</b> : {str(count).zfill(3)}\n"
            "**Video Title :** `{name1} [{res}p].{ext}`\n"
            "<blockquote><b>Batch Name :</b> {b_name}</blockquote>\n\n"
            "**Extracted by➤**{CR}</blockquote>\n\n"
            "**Caption Style 2**\n"
            "<blockquote expandable>**——— ✦ {str(count).zfill(3)} ✦ ———**\n\n"
            "🎞️ **Title** : `{name1}`\n"
            "**├── Extention :  {extension}.{ext}**\n"
            "**├── Resolution : [{res}]**\n"
            "📚 **Course : {b_name}**\n\n"
            "🌟 **Extracted By : {credit}**</blockquote>\n\n"
            "**Caption Style 3**\n"
            "<blockquote expandable>**{str(count).zfill(3)}.** {name1} [{res}p].{ext}</blockquote>\n\n"
            "**Send Your Caption Style eg. /cc1 or /cc2 or /cc3**", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.lower() == "/cc1":
                globals.caption = '/cc1'
                await editable.edit(f"✅ Caption Style 1 Updated!", reply_markup=keyboard)
            elif input_msg.text.lower() == "/cc2":
                globals.caption = '/cc2'
                await editable.edit(f"✅ Caption Style 2 Updated!", reply_markup=keyboard)
            else:
                globals.caption = input_msg.text
                await editable.edit(f"✅ Caption Style 3 Updated!", reply_markup=keyboard)
            
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set Caption Style:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("file_name_command"))
    async def handle_caption(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]])
        editable = await callback_query.message.edit("**Send End File Name or Send /d**", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.lower() == "/d":
                globals.endfilename = '/d'
                await editable.edit(f"✅ End File Name Disabled !", reply_markup=keyboard)
            else:
                globals.endfilename = input_msg.text
                await editable.edit(f"✅ End File Name `{globals.endfilename}` is enabled!", reply_markup=keyboard)            
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set End File Name:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("viideo_thumbnail_command"))
    async def video_thumbnail(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="thummbnail_command")]])
        editable = await callback_query.message.edit(f"Send the Video Thumb URL or Send /d \n<blockquote><b>Note </b>- For document format send : No</blockquote>", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.startswith("http://") or input_msg.text.startswith("https://"):
                globals.thumb = input_msg.text
                await editable.edit(f"✅ Thumbnail set successfully from the URL !", reply_markup=keyboard)
            elif input_msg.text.lower() == "/d":
                globals.thumb = "/d"
                await editable.edit(f"✅ Thumbnail set to default !", reply_markup=keyboard)
            else:
                globals.thumb = input_msg.text
                await editable.edit(f"✅ Video in Document Format is enabled !", reply_markup=keyboard)
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set thumbnail:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("pddf_thumbnail_command"))
    async def pdf_thumbnail_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="thummbnail_command")]])
      caption = ("<b>⋅ This Feature is Not Working Yet ⋅</b>")
      await callback_query.message.edit_media(
        InputMediaPhoto(
            media="https://envs.sh/GVI.jpg",
            caption=caption
        ),
        reply_markup=keyboard
      )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("add_credit_command"))
    async def credit(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]])
        editable = await callback_query.message.edit(f"Send Credit Name or Send /d", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.lower() == "/d":
                globals.CR = f"{CREDIT}"
                await editable.edit(f"✅ Credit set to default !", reply_markup=keyboard)
            else:
                globals.CR = input_msg.text
                await editable.edit(f"✅ Credit set as {globals.CR} !", reply_markup=keyboard)
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set Credit:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()

# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("cp_token_command"))
    async def handle_token(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="set_token_command")]])
        editable = await callback_query.message.edit("**Send Classplus Token**", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            globals.cptoken = input_msg.text
            await editable.edit(f"✅ Classplus Token set successfully !\n\n<blockquote expandable>`{globals.cptoken}`</blockquote>", reply_markup=keyboard)
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set Classplus Token:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....
    @bot.on_callback_query(filters.regex("cp_add_token_command"))
    async def handle_add_cp_token(client, callback_query):
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="set_token_command")]])
        editable = await callback_query.message.edit("**Send Classplus Token to Add**", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if globals.add_cptoken(input_msg.text):
                await editable.edit(f"✅ Token जोडला!\n\nTotal tokens: {len(globals.list_cptokens())}", reply_markup=keyboard)
            else:
                await editable.edit("⚠️ Token आधीपासून आहे किंवा invalid आहे.", reply_markup=keyboard)
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to add token:</b>\n<blockquote>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("cp_del_token_command"))
    async def handle_del_cp_token(client, callback_query):
        pool = globals.list_cptokens()
        if not pool:
            return await callback_query.message.edit("🚫 अजून tokens नाहीत.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="set_token_command")]]))
    
    # list दाखव
        text = "📌 Classplus Tokens:\n"
        for i, t in enumerate(pool):
            text += f"{i}: `{t[:8]}...{t[-8:]}`\n"
        text += "\n✍️ Send index number of token to delete."
    
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="set_token_command")]])
        editable = await callback_query.message.edit(text, reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            idx = int(input_msg.text)
            removed = globals.delete_cptoken(idx)
            if removed:
                await editable.edit(f"🗑️ Token काढला index {idx}", reply_markup=keyboard)
            else:
                await editable.edit("❌ चुकीचा index दिला.", reply_markup=keyboard)
        except Exception as e:
            await editable.edit(f"<b>❌ Failed:</b>\n<blockquote>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()

# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,

    @bot.on_callback_query(filters.regex("pw_token_command"))
    async def handle_token(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="set_token_command")]])
        editable = await callback_query.message.edit("**Send Physics Wallah Same Batch Token**", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            globals.pwtoken = input_msg.text
            await editable.edit(f"✅ Physics Wallah Token set successfully !\n\n<blockquote expandable>`{globals.pwtoken}`</blockquote>", reply_markup=keyboard) 
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set Physics Wallah Token:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("cw_token_command"))
    async def handle_token(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="set_token_command")]])
        editable = await callback_query.message.edit("**Send Carrerwill Token**", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.lower() == "/d":
                globals.cwtoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                await editable.edit(f"✅ Carrerwill Token set successfully as default !", reply_markup=keyboard)
            else:
                globals.cwtoken = input_msg.text
                await editable.edit(f"✅ Carrerwill Token set successfully !\n\n<blockquote expandable>`{globals.cwtoken}`</blockquote>", reply_markup=keyboard)      
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set Careerwill Token:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("video_wateermark_command"))
    async def video_watermark(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="wattermark_command")]])
        editable = await callback_query.message.edit(f"**Send Video Watermark text or Send /d**", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.lower() == "/d":
                globals.vidwatermark = "/d"
                await editable.edit(f"**Video Watermark Disabled ✅** !", reply_markup=keyboard)
            else:
                globals.vidwatermark = input_msg.text
                await editable.edit(f"Video Watermark `{globals.vidwatermark}` enabled ✅!", reply_markup=keyboard)
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set Watermark:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("pdf_wateermark_command"))
    async def pdf_watermark_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="wattermark_command")]])
      caption = ("<b>⋅ This Feature is Not Working Yet ⋅</b>")
      await callback_query.message.edit_media(
        InputMediaPhoto(
            media="https://envs.sh/GVI.jpg",
            caption=caption
        ),
        reply_markup=keyboard
      )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("quality_command"))
    async def handle_quality(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]])
        editable = await callback_query.message.edit("__**Enter resolution or Video Quality (`144`, `240`, `360`, `480`, `720`, `1080`) or Send /d**__", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.lower() == "144":
                globals.raw_text2 = '144'
                globals.quality = f"{globals.raw_text2}p"
                globals.res = '256x144'
                await editable.edit(f"✅ Video Quality set {globals.quality} !", reply_markup=keyboard)
            elif input_msg.text.lower() == "240":
                globals.raw_text2 = '240'
                globals.quality = f"{globals.raw_text2}p"
                globals.res = '426x240'
                await editable.edit(f"✅ Video Quality set {globals.quality} !", reply_markup=keyboard)
            elif input_msg.text.lower() == "360":
                globals.raw_text2 = '360'
                globals.quality = f"{globals.raw_text2}p"
                globals.res = '640x360'
                await editable.edit(f"✅ Video Quality set {globals.quality} !", reply_markup=keyboard)
            elif input_msg.text.lower() == "480":
                globals.raw_text2 = '480'
                globals.quality = f"{globals.raw_text2}p"
                globals.res = '854x480'
                await editable.edit(f"✅ Video Quality set {globals.quality} !", reply_markup=keyboard)
            elif input_msg.text.lower() == "720":
                globals.raw_text2 = '720'
                globals.quality = f"{globals.raw_text2}p"
                globals.res = '1280x720'
                await editable.edit(f"✅ Video Quality set {globals.quality} !", reply_markup=keyboard)
            elif input_msg.text.lower() == "1080":
                globals.raw_text2 = '1080'
                globals.quality = f"{globals.raw_text2}p"
                globals.res = '1920x1080'
                await editable.edit(f"✅ Video Quality set {globals.quality} !", reply_markup=keyboard)
            else:
                globals.raw_text2 = '480'
                globals.quality = f"{globals.raw_text2}p"
                globals.res = '854x480'
                await editable.edit(f"✅ Video Quality set {globals.quality} as Default !", reply_markup=keyboard)  
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set Video Quality:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("topic_command"))
    async def video_watermark(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]])
        editable = await callback_query.message.edit(f"**If you want to enable topic in caption: send /yes or send /d**\n\n<blockquote><b>Topic fetch from (bracket) in title</b></blockquote>", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.lower() == "/yes":               
                globals.topic = "/yes"
                await editable.edit(f"**Topic enabled in Caption ✅** !", reply_markup=keyboard)
            else:
                globals.topic = input_msg.text
                await editable.edit(f"Topic disabled in Caption ✅!", reply_markup=keyboard)
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to set Topic in Caption:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()

# ----------------- API Manager for Settings Panel -----------------

    SAVED_APIS_FILE = "saved_apis.json"

    def load_apis():
        if os.path.exists(SAVED_APIS_FILE):
            with open(SAVED_APIS_FILE, "r") as f:
                try:
                    return json.load(f)
                except:
                    return []
        return []

    def save_apis(data):
        with open(SAVED_APIS_FILE, "w") as f:
            json.dump(data, f, indent=2)


    # Callback to open Manage APIs menu (from Settings)
    @bot.on_callback_query(filters.regex("manage_apis"))
    async def manage_apis_cb(client, cq):
        user_id = cq.from_user.id
        apis = load_apis()

        if not apis:
            text = "⚠️ No saved APIs found."
        else:
            text = "📜 <b>Saved APIs:</b>\n\n" + "\n".join([f"{i+1}. {api}" for i, api in enumerate(apis)])

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add API", callback_data="manage_api_add"),
             InlineKeyboardButton("🗑 Delete API", callback_data="manage_api_del")],
            [InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]
        ])

        # Edit message (use edit or edit_media depending on your original message type)
        try:
            await cq.message.edit(text, reply_markup=keyboard, disable_web_page_preview=True)
        except:
            # fallback to sending a new message if edit fails
            await cq.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True)


    # Handler for Add API (button)
    @bot.on_callback_query(filters.regex("manage_api_add"))
    async def manage_api_add_cb(client, cq):
        user_id = cq.from_user.id
        await cq.message.edit("✏️ Send the new API URL to add:\n\n(eg: https://myapi.example/extract?url={url}&token={cptoken})",
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))
        # listen to the same user who clicked
        new_api_msg = await bot.listen(user_id)
        new_api = new_api_msg.text.strip()

        try:
            apis = load_apis()

            if not new_api.startswith("http"):
                await cq.message.edit("⚠️ Invalid API URL. Must start with http/https.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))
                return

            if new_api in apis:
                await cq.message.edit("⚠️ This API already exists in the list.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))
                return

            apis.append(new_api)
            save_apis(apis)
            await cq.message.edit(f"✅ API added successfully!\n\nTotal APIs: {len(apis)}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))
        except Exception as e:
            await cq.message.edit(f"❌ Failed to add API:\n{e}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))
        finally:
            # cleanup user message to avoid clutter
            try:
                await new_api_msg.delete()
            except:
                pass


    # Handler for Delete API (button)
    @bot.on_callback_query(filters.regex("manage_api_del"))
    async def manage_api_del_cb(client, cq):
        user_id = cq.from_user.id
        apis = load_apis()

        if not apis:
            await cq.message.edit("⚠️ No saved APIs found.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))
            return

        api_list = "\n".join([f"{i+1}. {api}" for i, api in enumerate(apis)])
        await cq.message.edit(f"🗑 Saved APIs:\n{api_list}\n\n✍️ Send the number (index) to delete:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))

        choice_msg = await bot.listen(user_id)
        try:
            idx = int(choice_msg.text.strip()) - 1
            if idx < 0 or idx >= len(apis):
                raise ValueError("invalid index")

            removed = apis.pop(idx)
            save_apis(apis)
            await cq.message.edit(f"✅ Deleted API:\n{removed}\n\nTotal APIs left: {len(apis)}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))
        except Exception as e:
            await cq.message.edit("⚠️ Invalid selection or error.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="manage_apis")]]))
        finally:
            try:
                await choice_msg.delete()
            except:
                pass

# ----------------- End API Manager -----------------

    @bot.on_callback_query(filters.regex("resset_command"))
    async def credit(client, callback_query):
        user_id = callback_query.from_user.id
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Settings", callback_data="setttings")]])
        editable = await callback_query.message.edit(f"If you want to reset settings send /yes or Send /no", reply_markup=keyboard)
        input_msg = await bot.listen(editable.chat.id)
        try:
            if input_msg.text.lower() == "/yes":
                globals.caption = '/cc1'
                globals.endfilename = '/d'
                globals.thumb = '/d'
                globals.CR = f"{CREDIT}"
                globals.cwtoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                globals.cptoken = "cptoken"
                globals.pwtoken = "pwtoken"
                globals.vidwatermark = '/d'
                globals.raw_text2 = '480'
                globals.quality = '480p'
                globals.res = '854x480'
                globals.topic = '/d'
                await editable.edit(f"✅ Settings reset as default !", reply_markup=keyboard)
            else:
                await editable.edit(f"✅ Settings Not Changed !", reply_markup=keyboard)
        except Exception as e:
            await editable.edit(f"<b>❌ Failed to Change Settings:</b>\n<blockquote expandable>{str(e)}</blockquote>", reply_markup=keyboard)
        finally:
            await input_msg.delete()

# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
