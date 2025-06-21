from telegram import Update
from telegram.ext import ContextTypes
from config import HELP_IMAGE

HELP_TEXT = (
    "💡 *Cozy Command Guide:*\n"
    "/start - Introduce the bot with buttons\n"
    "/help - Show this help message\n"
    "/ping - Check if I'm alive~\n"
    "Mention me in groups to ask questions!"
)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=HELP_IMAGE,
        caption=HELP_TEXT,
        parse_mode="Markdown"
    )

async def help_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_photo(
        photo=HELP_IMAGE,
        caption=HELP_TEXT,
        parse_mode="Markdown"
    )
