from database import add_user, get_user


def run(bot, message):
    user_id = message.from_user.id

    add_user(user_id)
    user = get_user(user_id)

    if not user:
        bot.send_message(message.chat.id, "Ошибка баланса")
        return

    balance = user["balance"]
    cookies = user["cookies"]

    text = (
        f"💰 Баланс\n\n"
        f"💵 Деньги: {balance}\n"
        f"🍪 Печеньки: {cookies}"
    )

    bot.send_message(message.chat.id, text)
