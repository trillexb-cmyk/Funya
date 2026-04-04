from loader import bot

@bot.message_handler(func=lambda m: m.text == "🎒 Инвентарь")
def inventory(m):
    bot.send_message(m.chat.id, "🎒 Инвентарь\n🚧 Раздел в разработке")
