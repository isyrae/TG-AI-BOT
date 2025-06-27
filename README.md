<h1 align="center">🧠 TG-AI-BOT</h1>
<p align="center">
  <img src="https://files.catbox.moe/gq66gs.png" width="500"/>
</p>
<p align="center">
  <b>A modern Telegram AI chatbot built by <a href="https://t.me/isyraeprojects">@isyrae</a></b><br>
  Powered by Pyrogram + OpenRouter AI + personality engine<br><br>
  <a href="https://t.me/isyraebot">🤖 Try Demo Bot</a> •
  <a href="https://t.me/isyraeprojects">📦 Dev Channel</a> •
  <a href="https://github.com/isyrae/TG-AI-BOT/blob/main/LICENSE">📄 MIT License</a>
</p>

---

## 🔥 Features

- 🤖 **AI Chat** powered by [OpenRouter API](https://openrouter.ai)
- 🧠 Remembers conversations (per user)
- 🖼️ Image-based replies for `/start`, `/help`, `/ping`
- 🔐 Per-user rate limiting
- 🛠️ Group & private chat support
- 📊 Logging, admin-only commands, and support links
- 🌐 English + Hindi support
- ✨ Fully modular and beginner-friendly

---

## 📁 Environment Setup

Create a `.env` file in the root folder:

```env
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
OPENROUTER_API_KEY=YOUR_OPENROUTER_APIKEY_HERE
SUPPORT_LINK=https://t.me/isyraeprojects
BOT_USERNAME=AskCozyBot
START_IMAGE=https://files.catbox.moe/gq66gs.png
HELP_IMAGE=https://files.catbox.moe/gq66gs.png
PING_IMAGE=https://files.catbox.moe/gq66gs.png
```

---

## 🧰 Requirements

Make sure Python 3.10+ is installed. Then run:

```bash
apt update && apt install python3.10 python3-pip -y
pip3 install -r requirements.txt
```

---

## 🚀 How to Deploy

```bash
# Go to project folder
cd /www/wwwroot/cozyai

# Run the bot
python3.10 main.py
```

✅ The bot will respond to:

- `/start` → Sends welcome card with buttons  
- `/help` → Sends help image and text  
- `/ping` → Shows bot latency  
- Mentions of “Cozy” or its username in groups  

## 🌐 Links

- 🤖 Bot: [@isyraebot](https://t.me/askcozybot)  
- 📦 Channel: [@isyraeprojects](https://t.me/isyraeprojects)  
- 👨‍💻 Author: [isyrae](https://github.com/isyrae)  
- 📝 License: [MIT](LICENSE)

---

## 🧾 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it **with credit**.

---

### ❤️ Powered by [@isyrae](https://t.me/isyraeprojects) — Bots, Tools & Automation for Everyone
