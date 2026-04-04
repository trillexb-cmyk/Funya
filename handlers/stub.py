def register_handlers(bot):
    @bot.message_handler(func=lambda m: True)
    def stub_command(message):
        if message.text not in ["👤 Профиль", "🎁 Бонус"]:
            bot.send_message(message.chat.id, "🚧 Раздел в разработке")
