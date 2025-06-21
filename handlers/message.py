from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from config import BOT_USERNAME
from utils.kawaii_ai import get_kawaii_reply
from utils.rate_limiter import is_rate_limited
import asyncio

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()
    chat_type = update.message.chat.type

    if chat_type != "private":
        if BOT_USERNAME.lower() not in text.lower() and "cozy" not in text.lower():
            return

    wait = is_rate_limited(user_id)
    if wait > 0:
        await update.message.reply_text(f"⏱️ Aww~ wait {wait}s before asking again 💖")
        return

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(1.2)
    reply = await get_kawaii_reply(text)
    await update.message.reply_text(reply)
