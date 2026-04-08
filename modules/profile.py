from database import add_user, get_user


def run(bot, message):
    user_id = message.from_user.id

    add_user(user_id)
    user = get_user(user_id)

    if not user:
        bot.send_message(message.chat.id, "Ошибка профиля")
        return

    text = (
        f"👤 Профиль\n\n"
        f"🆔 ID: {user['user_id']}\n"
        f"💰 Баланс: {user['balance']}\n\n"

        f"🏆 Уровень: {user['level']}\n"
        f"⚡ Опыт: {user['exp']}\n\n"

        f"💬 Сообщения: {user['messages']}\n"
        f"⭐ Репутация: {user['reputation']}\n\n"

        f"👥 Клан: {user['clan']}\n"
        f"💍 Партнёр: {user['partner'] if user['partner'] else 'нет'}"
    )

    bot.send_message(message.chat.id, text)
