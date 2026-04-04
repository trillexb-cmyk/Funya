def register_handlers(bot):
    @bot.message_handler(func=lambda m: m.chat.type != "private")
    def chat_welcome(message):
        bot.send_message(message.chat.id,
                         "👋 Привет! Я Фуня — ваш развлекательный бот!\n\n"
                         "Хочешь узнать, что я умею?\n"
                         "Напиши: фуня помощь или команды")
