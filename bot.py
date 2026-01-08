import asyncio
from pyrogram import Client, filters
from character import get_reply
from memory import remember, recall

app = Client("catlakbot")

@app.on_message(filters.text & ~filters.bot)
async def handle(client, message):
    user_id = message.from_user.id
    remember(user_id, message.text)
    reply = await get_reply(message.text, recall(user_id), message.chat.type)
    await message.reply_text(reply)

async def main():
    await app.start()
    print("Bot is running...")
    await app.idle()

if __name__ == "__main__":
    asyncio.run(main())
