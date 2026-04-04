from loader import bot

@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith("обнять"))
def hug(m):
    if m.reply_to_message:
        bot.send_message(
            m.chat.id,
            f"{m.from_user.first_name} обнял {m.reply_to_message.from_user.first_name}"
        )
