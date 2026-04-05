from database import add_user, get_user


def show_profile(bot, message):
    user_id = message.from_user.id

    add_user(user_id)
    user = get_user(user_id)

    bot.send_message(
        message.chat.id,
        f"👤 Профиль\n\n"
        f"🆔 {user_id}\n"
        f"💰 Баланс: {user[1]}\n"
        f"🍪 Печеньки: {user[2]}"
    )
