from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import START_IMAGE, SUPPORT_LINK

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("➕ Add me to your GC", url=f"https://t.me/{context.bot.username}?startgroup=true")],
        [InlineKeyboardButton("📘 Help", callback_data="show_help")],
        [InlineKeyboardButton("🎧 Support", url=SUPPORT_LINK)]
    ]
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=START_IMAGE,
        caption="Heyy nya~ 💖 I'm your cozy assistant! Ask me anything or click below~ ✨",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
