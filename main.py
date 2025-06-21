from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import BOT_TOKEN
from handlers.start import start_cmd
from handlers.help import help_cmd, help_button_callback
from handlers.ping import ping_cmd
from handlers.message import handle_text

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping_cmd))
    app.add_handler(CallbackQueryHandler(help_button_callback, pattern="^show_help$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("🌸 Cozy AI bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
