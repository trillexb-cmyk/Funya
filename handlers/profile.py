from database import get_user, add_user

def show_profile(bot, message):
    user_id = message.from_user.id
    add_user(user_id)

    user = get_user(user_id)

    text = f"""👤 Твой профиль

ID: {user[0]}
Баланс: {user[1]} 🍬 Фунтиков
🍪 Печенек: {user[2]}

Характеристика: 0"""

    if user[4]:
        text += f"\n\nПара: {user[4]}"

    text += f"\nКлан: {user[3]}"

    bot.send_message(message.chat.id, text)
