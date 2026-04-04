import os
import sqlite3
import psycopg
import time
from config import USE_POSTGRES

if USE_POSTGRES:
    conn = psycopg.connect(os.environ.get("DATABASE_URL"))
    cursor = conn.cursor()
else:
    conn = sqlite3.connect("funya.db", check_same_thread=False)
    cursor = conn.cursor()

# ===== СОЗДАНИЕ ТАБЛИЦЫ =====
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    balance INT DEFAULT 500,
    cookies INT DEFAULT 2000,
    clan TEXT DEFAULT 'отсутствует',
    partner TEXT DEFAULT NULL
)
""")
conn.commit()

# ===== ДОБАВЛЕНИЕ КОЛОНКИ (ЕСЛИ НЕТ) =====
try:
    cursor.execute("ALTER TABLE users ADD COLUMN last_bonus BIGINT DEFAULT 0")
    conn.commit()
except:
    pass  # если колонка уже есть — просто игнорируем


# ===== ФУНКЦИИ =====
def add_user(user_id):
    if USE_POSTGRES:
        cursor.execute(
            "INSERT INTO users (user_id) VALUES (%s) ON CONFLICT DO NOTHING",
            (user_id,)
        )
    else:
        cursor.execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,)
        )
    conn.commit()


def get_user(user_id):
    if USE_POSTGRES:
        cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
    else:
        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()


def update_balance(user_id, amount):
    if USE_POSTGRES:
        cursor.execute(
            "UPDATE users SET balance = balance + %s WHERE user_id=%s",
            (amount, user_id)
        )
    else:
        cursor.execute(
            "UPDATE users SET balance = balance + ? WHERE user_id=?",
            (amount, user_id)
        )
    conn.commit()


def get_last_bonus(user_id):
    if USE_POSTGRES:
        cursor.execute("SELECT last_bonus FROM users WHERE user_id=%s", (user_id,))
    else:
        cursor.execute("SELECT last_bonus FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0


def update_last_bonus(user_id):
    now = int(time.time())
    if USE_POSTGRES:
        cursor.execute(
            "UPDATE users SET last_bonus=%s WHERE user_id=%s",
            (now, user_id)
        )
    else:
        cursor.execute(
            "UPDATE users SET last_bonus=? WHERE user_id=?",
            (now, user_id)
        )
    conn.commit()
