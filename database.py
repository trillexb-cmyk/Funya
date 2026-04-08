import os
import sqlite3
import psycopg
import time
import threading
from config import USE_POSTGRES


lock = threading.Lock()


# ===== ПОДКЛЮЧЕНИЕ =====
if USE_POSTGRES:
    conn = psycopg.connect(os.environ.get("DATABASE_URL"))
    conn.autocommit = True
else:
    conn = sqlite3.connect("funya.db", check_same_thread=False)


# ===== EXECUTE =====
def execute(query, params=None, fetchone=False, fetchall=False):
    with lock:
        try:
            cur = conn.cursor()
            cur.execute(query, params or ())

            if fetchone:
                row = cur.fetchone()
                if not row:
                    return None

                columns = [desc[0] for desc in cur.description]
                return dict(zip(columns, row))

            if fetchall:
                rows = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                return [dict(zip(columns, r)) for r in rows]

            if not USE_POSTGRES:
                conn.commit()

        except Exception as e:
            print("DB ERROR:", e)
            try:
                conn.rollback()
            except:
                pass


# ===== СОЗДАНИЕ ТАБЛИЦЫ =====
execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY
)
""")


# ===== КОЛОНКИ =====
def safe_column(query):
    try:
        execute(query)
    except:
        pass


safe_column("ALTER TABLE users ADD COLUMN balance INT DEFAULT 500")
safe_column("ALTER TABLE users ADD COLUMN cookies INT DEFAULT 2000")
safe_column("ALTER TABLE users ADD COLUMN clan TEXT DEFAULT 'отсутствует'")
safe_column("ALTER TABLE users ADD COLUMN partner TEXT DEFAULT NULL")
safe_column("ALTER TABLE users ADD COLUMN last_bonus BIGINT DEFAULT 0")

safe_column("ALTER TABLE users ADD COLUMN exp INT DEFAULT 0")
safe_column("ALTER TABLE users ADD COLUMN level INT DEFAULT 1")
safe_column("ALTER TABLE users ADD COLUMN reputation INT DEFAULT 0")
safe_column("ALTER TABLE users ADD COLUMN messages INT DEFAULT 0")
safe_column("ALTER TABLE users ADD COLUMN warns INT DEFAULT 0")
safe_column("ALTER TABLE users ADD COLUMN mute_until BIGINT DEFAULT 0")


# ===== ПОЛЬЗОВАТЕЛЬ =====
def add_user(user_id):
    if USE_POSTGRES:
        execute(
            "INSERT INTO users (user_id) VALUES (%s) ON CONFLICT DO NOTHING",
            (user_id,)
        )
    else:
        execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,)
        )


def get_user(user_id):
    if USE_POSTGRES:
        return execute(
            "SELECT * FROM users WHERE user_id=%s",
            (user_id,),
            fetchone=True
        )
    else:
        return execute(
            "SELECT * FROM users WHERE user_id=?",
            (user_id,),
            fetchone=True
        )


# ===== БАЛАНС =====
def update_balance(user_id, amount):
    if USE_POSTGRES:
        execute(
            "UPDATE users SET balance = balance + %s WHERE user_id=%s",
            (amount, user_id)
        )
    else:
        execute(
            "UPDATE users SET balance = balance + ? WHERE user_id=?",
            (amount, user_id)
        )


# ===== БОНУС =====
def get_last_bonus(user_id):
    user = get_user(user_id)
    return user["last_bonus"] if user else 0


def update_last_bonus(user_id):
    now = int(time.time())

    if USE_POSTGRES:
        execute(
            "UPDATE users SET last_bonus=%s WHERE user_id=%s",
            (now, user_id)
        )
    else:
        execute(
            "UPDATE users SET last_bonus=? WHERE user_id=?",
            (now, user_id)
        )


# ===== ДОП =====
def add_exp(user_id, amount):
    if USE_POSTGRES:
        execute(
            "UPDATE users SET exp = exp + %s WHERE user_id=%s",
            (amount, user_id)
        )
    else:
        execute(
            "UPDATE users SET exp = exp + ? WHERE user_id=?",
            (amount, user_id)
        )


def add_message(user_id):
    if USE_POSTGRES:
        execute(
            "UPDATE users SET messages = messages + 1 WHERE user_id=%s",
            (user_id,)
        )
    else:
        execute(
            "UPDATE users SET messages = messages + 1 WHERE user_id=?",
            (user_id,)
        )


# ===== РЕСЕТ =====
def reset_db():
    execute("DELETE FROM users")
