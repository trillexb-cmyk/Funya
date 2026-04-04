ACTIONS = {
    "обнять": "🤗",
    "поцеловать": "😘",
    "укусить": "🧛",
    "шлепнуть": "😂",
    "пнуть": "🦶",
    "подмигнуть": "😉",
    "погладить": "🥰",
    "подтолкнуть": "😄",
    "пожать": "🤝",
    "похлопать": "👏"
}

def register_handlers(bot):
    @bot.message_handler(func=lambda m: m.text.lower() in ACTIONS)
    def social_action(message):
        if message.reply_to_message:
            target = message.reply_to_message.from_user.username or message.reply_to_message.from_user.first_name
            sender = message.from_user.username or message.from_user.first_name
            emoji = ACTIONS[message.text.lower()]
            bot.send_message(message.chat.id, f"@{sender} {message.text.lower()} @{target} {emoji}")
        else:
            bot.send_message(message.chat.id, "⚠️ Используй это как ответ на сообщение другого пользователя или с упоминанием @User")
