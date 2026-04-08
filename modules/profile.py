from database import add_user, get_user


def run(bot, message):
    user_id = message.from_user.id

    add_user(user_id)
    user = get_user(user_id)

    if not user:
        bot.send_message(message.chat.id, "Ошибка профиля")
        return

    (
        uid,
        balance,
        cookies,
        clan,
        partner,
        last_bonus,
        exp,
        level,
        reputation,
        messages,
        warns,
        mute_until
    ) = user

    text = (
        f"👤 Профиль\n\n"
        f"🆔 ID: {uid}\n"
        f"💰 Баланс: {balance}\n\n"

        f"🏆 Уровень: {level}\n"
        f"⚡ Опыт: {exp}\n\n"

        f"💬 Сообщения: {messages}\n"
        f"⭐ Репутация: {reputation}\n\n"

        f"👥 Клан: {clan}\n"
        f"💍 Партнёр: {partner if partner else 'нет'}"
    )

    bot.send_message(message.chat.id, text)
