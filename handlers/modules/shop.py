from loader import bot

@bot.message_handler(func=lambda m: m.text == "🛒 Магазин")
def shop(m):
    bot.send_message(m.chat.id, "🛒 Магазин\n🚧 Раздел в разработке")
