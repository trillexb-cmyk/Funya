import time
from database import add_user, get_last_bonus, update_last_bonus, update_balance


BONUS = 2500
COOLDOWN = 86400  # 24 часа


def run(bot, message):
    user_id = message.from_user.id

    add_user(user_id)

    last = get_last_bonus(user_id)
    now = int(time.time())

    diff = now - last

    # ===== ЕСЛИ МОЖНО =====
    if diff >= COOLDOWN:
        update_balance(user_id, BONUS)
        update_last_bonus(user_id)

        bot.send_message(
            message.chat.id,
            f"🎁 Бонус получен!\n\n"
            f"💰 +{BONUS}"
        )
        return

    # ===== ЕСЛИ НЕЛЬЗЯ =====
    remaining = COOLDOWN - diff

    h = remaining // 3600
    m = (remaining % 3600) // 60

    bot.send_message(
        message.chat.id,
        f"⏳ Бонус уже получен\n\n"
        f"⌛ Осталось: {h}ч {m}м"
    )
