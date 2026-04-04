from database import get_user, add_user


def show_profile(bot, message):
    user_id = message.from_user.id

    user = get_user(user_id)

    if not user:
        add_user(user_id)
        user = get_user(user_id)

    balance = user[1]
    cookies = user[2]
    clan = user[3]
    partner = user[4]

    text = (
        f"👤 Профиль\n\n"
        f"🆔 Айди: {user_id}\n"
        f"💰 Баланс: {balance} 🍬Фунтиков\n"
        f"🍪 Печенек: {cookies}\n"
        f"⚒ Характеристика: 0\n"
    )

    if partner:
        text += f"💑 Пара: {partner}\n"

    text += f"🏰 Клан: {clan}\n"

    bot.send_message(message.chat.id, text)
