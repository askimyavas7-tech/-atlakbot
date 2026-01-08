from pyrogram import Client, filters
from character import get_reply
from memory import remember, recall

app = Client("catlakbot")

@app.on_message(filters.text & ~filters.bot)
def handle(client, message):
    user_id = message.from_user.id
    remember(user_id, message.text)
    reply = get_reply(message.text, recall(user_id), message.chat.type)
    message.reply_text(reply)

app.run()
