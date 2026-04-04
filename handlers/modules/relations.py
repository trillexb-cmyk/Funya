from loader import bot

@bot.message_handler(func=lambda m: m.text == "❤️ Отношения")
def relations(m):
    bot.send_message(m.chat.id, "❤️ Отношения\n🚧 Раздел в разработке")
