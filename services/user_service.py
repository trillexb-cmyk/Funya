from database import cursor
from datetime import datetime
import pytz

KYIV = pytz.timezone("Europe/Kyiv")

def today():
    return datetime.now(KYIV).strftime("%Y-%m-%d")

def get_user(uid):
    cursor.execute("SELECT * FROM users WHERE user_id=%s", (uid,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO users (user_id) VALUES (%s)", (uid,))
        return get_user(uid)

    return user

def get_balance(uid):
    return get_user(uid)[1]

def transfer_balance(a, b, amount):
    if amount <= 0:
        return False
    if get_balance(a) < amount:
        return False

    get_user(b)

    cursor.execute("UPDATE users SET coins=coins-%s WHERE user_id=%s", (amount, a))
    cursor.execute("UPDATE users SET coins=coins+%s WHERE user_id=%s", (amount, b))
    return True

def can_bonus(uid):
    return get_user(uid)[4] != today()

def give_bonus(uid):
    cursor.execute(
        "UPDATE users SET coins=coins+2500,last_bonus_date=%s WHERE user_id=%s",
        (today(), uid)
    )

def get_inventory(uid):
    data = get_user(uid)[2]
    return data.split(",") if data else []

def get_relationship(uid):
    return get_user(uid)[3]
