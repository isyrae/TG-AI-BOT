from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
SUPPORT_LINK = os.getenv("SUPPORT_LINK")
BOT_USERNAME = os.getenv("BOT_USERNAME")
START_IMAGE = os.getenv("START_IMAGE")
HELP_IMAGE = os.getenv("HELP_IMAGE")
PING_IMAGE = os.getenv("PING_IMAGE")

MODEL = "meta-llama/llama-3-8b-instruct"
