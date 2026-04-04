from database import get_user, create_user


def show_profile(bot, message):
    user_id = message.from_user.id

    # получаем или создаём пользователя
    user = get_user(user_id)

    if not user:
        create_user(user_id)
        user = get_user(user_id)

    # данные
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

    if clan:
        text += f"🏰 Клан: {clan}\n"
    else:
        text += f"🏰 Клан: отсутствует\n"

    bot.send_message(message.chat.id, text)
