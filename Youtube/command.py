from pyrogram import Client, filters
import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe

# Calculate current time greeting
currentTime = datetime.datetime.now()
if currentTime.hour < 12:
    wish = "Hayrli Tong ! 🌞"
elif 12 <= currentTime.hour < 18:
    wish = "Hayrli Kun ! 🌤️"
else:
    wish = "Hayrli Kech ! 🌝"

@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

# About command handler
@Client.on_message(filters.private & filters.command("about"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    await message.reply_text(
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('⛔️ Close', callback_data='cancel')]
        ]
    ))


# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    #user = message.from_user
    await message.reply_text(
        text=Translation.START_TEXT.format(message.from_user.first_name, wish),
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📍 Update Channel', url='https://t.me/kmaxProgrammers'),
            ],
            [
                InlineKeyboardButton('👩‍💻 Developer', url='https://t.me/kmaxProgrammers'),
                InlineKeyboardButton('👥 Support Group', url='https://t.me/kmaxProgrammers'),
            ],
            [
                InlineKeyboardButton('⛔️ Close', callback_data='cancel')
            ]
        ]
    ))

# Help command handler
@Client.on_message(filters.command("help"))
async def help(client, message):
    help_text = """
YouTube video yuklovchi botiga xush kelibsiz!

YouTube videosini yuklash uchun menga YouTube havolasini yuboring.

Botdan zavqlaning!

©️ Channel : @kmaxProgrammers
    """
    await message.reply_text(help_text)
