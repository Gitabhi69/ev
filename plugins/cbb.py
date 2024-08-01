#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<a href='https://t.me/+_2pULQF1-hQzYzJl'>Evolution Series ⚡️</a> \n\nI am a Telegram Bot for storing posts or files that can be accessed via a special link.\n\n• Creator : @It_was_abhi \n• Language : <code>Python3</code>\n• Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio 0.3</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
