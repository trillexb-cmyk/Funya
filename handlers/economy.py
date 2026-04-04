from database import update_balance, get_last_bonus, update_last_bonus, add_user
import time

BONUS_AMOUNT = 2500
COOLDOWN = 86400  # 24 часа


def get_bonus(bot, message):
    user_id = message.from_user.id
    add_user(user_id)

    last_bonus = get_last_bonus(user_id)
    now = int(time.time())

    if now - last_bonus < COOLDOWN:
        remaining = COOLDOWN - (now - last_bonus)
        hours = remaining // 3600
        minutes = (remaining % 3600) // 60

        bot.send_message(
            message.chat.id,
            f"⏳ Бонус уже получен\nПопробуй через {hours}ч {minutes}м"
        )
        return

    update_balance(user_id, BONUS_AMOUNT)
    update_last_bonus(user_id)

    bot.send_message(
        message.chat.id,
        "🎁 Бонус\n\n+2500 💰"
    )


def show_balance(bot, message):
    from database import get_user
    user = get_user(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f"💰 Баланс: {user[1]} 🍬\n🍪 Печеньки: {user[2]}"
    )
