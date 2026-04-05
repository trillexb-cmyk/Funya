from telebot import types


def run(bot, message):
    # проверка: есть ли ответ на сообщение
    if not message.reply_to_message:
        bot.send_message(
            message.chat.id,
            "❌ Ответь на сообщение пользователя, чтобы забанить"
        )
        return

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    try:
        # бан пользователя
        bot.ban_chat_member(chat_id, user_id)

        bot.send_message(
            chat_id,
            f"🔨 Пользователь забанен"
        )

    except Exception as e:
        bot.send_message(
            chat_id,
            "❌ Ошибка бана (проверь права бота)"
        )
        print("BAN ERROR:", e)
