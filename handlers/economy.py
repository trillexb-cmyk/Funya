import time
from datetime import datetime, timedelta
import pytz

from database import (
    add_user,
    get_user,
    update_balance,
    get_last_bonus,
    update_last_bonus
)

from config import TIMEZONE


# ===== БАЛАНС =====
def show_balance(bot, message):
    user_id = message.from_user.id
    add_user(user_id)

    user = get_user(user_id)

    balance = user[1]
    cookies = user[2]

    bot.send_message(
        message.chat.id,
        f"💰 Баланс: {balance}\n🍪 Печеньки: {cookies}"
    )


# ===== ЕЖЕДНЕВНЫЙ БОНУС =====
def get_bonus(bot, message):
    user_id = message.from_user.id
    add_user(user_id)

    tz = pytz.timezone(TIMEZONE)
    now = datetime.now(tz)

    last_ts = get_last_bonus(user_id)

    # ===== ЕСЛИ ВПЕРВЫЕ =====
    if last_ts == 0:
        give_bonus(bot, message, user_id)
        return

    last = datetime.fromtimestamp(last_ts, tz)

    # ===== ЕСЛИ НОВЫЙ ДЕНЬ =====
    if last.date() != now.date():
        give_bonus(bot, message, user_id)
        return

    # ===== СЧИТАЕМ ДО 00:00 =====
    tomorrow = now + timedelta(days=1)

    next_midnight = datetime(
        year=tomorrow.year,
        month=tomorrow.month,
        day=tomorrow.day,
        hour=0,
        minute=0,
        second=0,
        tzinfo=tz
    )

    remaining = next_midnight - now

    hours = remaining.seconds // 3600
    minutes = (remaining.seconds % 3600) // 60

    bot.send_message(
        message.chat.id,
        f"⏳ Бонус уже получен\n"
        f"Попробуй через {hours}ч {minutes}м"
    )


# ===== ВЫДАЧА БОНУСА =====
def give_bonus(bot, message, user_id):
    reward = 2500

    update_balance(user_id, reward)
    update_last_bonus(user_id)

    bot.send_message(
        message.chat.id,
        f"🎁 Ежедневный бонус\n+{reward} 💰"
    )


# ===== ПЕРЕВОД (заглушка) =====
def transfer(bot, message):
    bot.send_message(
        message.chat.id,
        "🔄 Переводы\n\n🚧 В разработке"
            )
