from telegram import Update
from telegram.ext import ContextTypes
from config import PING_IMAGE

async def ping_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=PING_IMAGE,
        caption="Pong~ nyaaa! 🐾 I’m alive and ready to help 💖"
    )
