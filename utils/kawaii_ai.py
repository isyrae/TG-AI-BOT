import aiohttp
from config import MODEL, OPENROUTER_API_KEY

BOT_PERSONALITY = (
    "You are a super cute, cozy, and intelligent AI assistant. "
    "You speak like a kawaii anime character, using emojis and sweet expressions. "
    "Your tone is always bubbly, adorable, and friendly, with occasional Hindi like 'aww kya sweet hai~ 💖'. "
    "You're very helpful, smart, and always polite!"
)

async def get_kawaii_reply(user_message: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": BOT_PERSONALITY},
            {"role": "user", "content": user_message}
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload) as resp:
            data = await resp.json()
            if 'choices' in data:
                return f"🌸 {data['choices'][0]['message']['content'].strip()} 🌸"
            return "Ughh~ I'm a bit confused nyah~ 💭"
