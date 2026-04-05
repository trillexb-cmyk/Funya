import os
import sqlite3
import psycopg
import time
from config import USE_POSTGRES

# ===== ПОДКЛЮЧЕНИЕ =====
if USE_POSTGRES:
    conn = psycopg.connect(os.environ.get("DATABASE_URL"))
    conn.autocommit = True  # 🔥 УБИРАЕТ ПРОБЛЕМУ С ТРАНЗАКЦИЯМИ
    cursor = conn.cursor()
else:
    conn = sqlite3.connect("funya.db", check_same_thread=False)
    cursor = conn.cursor()


# ===== БЕЗОПАСНОЕ ВЫПОЛНЕНИЕ =====
def safe_execute(query, params=None):
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
    except Exception as e:
        print("DB ERROR:", e)
        if not USE_POSTGRES:
            conn.rollback()


# ===== СОЗДАНИЕ ТАБЛИЦЫ =====
safe_execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY
)
""")


# ===== АВТО-ОБНОВЛЕНИЕ КОЛОНОК =====
def safe_column(query):
    try:
        cursor.execute(query)
    except:
        pass


safe_column("ALTER TABLE users ADD COLUMN balance INT DEFAULT 500")
safe_column("ALTER TABLE users ADD COLUMN cookies INT DEFAULT 2000")
safe_column("ALTER TABLE users ADD COLUMN clan TEXT DEFAULT 'отсутствует'")
safe_column("ALTER TABLE users ADD COLUMN partner TEXT DEFAULT NULL")
safe_column("ALTER TABLE users ADD COLUMN last_bonus BIGINT DEFAULT 0")


# ===== ПОЛЬЗОВАТЕЛЬ =====
def add_user(user_id):
    if USE_POSTGRES:
        safe_execute(
            "INSERT INTO users (user_id) VALUES (%s) ON CONFLICT DO NOTHING",
            (user_id,)
        )
    else:
        safe_execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,)
        )


def get_user(user_id):
    if USE_POSTGRES:
        safe_execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
    else:
        safe_execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()


# ===== БАЛАНС =====
def update_balance(user_id, amount):
    if USE_POSTGRES:
        safe_execute(
            "UPDATE users SET balance = balance + %s WHERE user_id=%s",
            (amount, user_id)
        )
    else:
        safe_execute(
            "UPDATE users SET balance = balance + ? WHERE user_id=?",
            (amount, user_id)
        )


# ===== БОНУС =====
def get_last_bonus(user_id):
    if USE_POSTGRES:
        safe_execute("SELECT last_bonus FROM users WHERE user_id=%s", (user_id,))
    else:
        safe_execute("SELECT last_bonus FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0


def update_last_bonus(user_id):
    now = int(time.time())
    if USE_POSTGRES:
        safe_execute(
            "UPDATE users SET last_bonus=%s WHERE user_id=%s",
            (now, user_id)
        )
    else:
        safe_execute(
            "UPDATE users SET last_bonus=? WHERE user_id=?",
            (now, user_id)
        )


# ===== РЕСЕТ БД =====
def reset_db():
    safe_execute("DELETE FROM users")
