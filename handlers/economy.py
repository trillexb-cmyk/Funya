import time
from database import add_user, update_balance, get_user


def show_balance(bot, message):
    user_id = message.from_user.id
    add_user(user_id)

    user = get_user(user_id)

    bot.send_message(
        message.chat.id,
        f"💰 Баланс: {user[1]}"
    )


def get_bonus(bot, message):
    user_id = message.from_user.id
    add_user(user_id)

    reward = 2500
    update_balance(user_id, reward)

    bot.send_message(
        message.chat.id,
        f"🎁 Ты получил {reward} монет!"
    )
