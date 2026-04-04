import os
import sqlite3
import psycopg  # psycopg3
from config import USE_POSTGRES

if USE_POSTGRES:
    # подключение к PostgreSQL
    conn = psycopg.connect(os.environ.get("DATABASE_URL"))
    cursor = conn.cursor()
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
else:
    # SQLite
    conn = sqlite3.connect("funya.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        balance INTEGER DEFAULT 500,
        cookies INTEGER DEFAULT 2000,
        clan TEXT DEFAULT 'отсутствует',
        partner TEXT DEFAULT NULL
    )
    """)
    conn.commit()


def add_user(user_id):
    if USE_POSTGRES:
        cursor.execute("INSERT INTO users (user_id) VALUES (%s) ON CONFLICT DO NOTHING", (user_id,))
    else:
        cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()


def get_user(user_id):
    if USE_POSTGRES:
        cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
    else:
        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()


def update_balance(user_id, amount):
    if USE_POSTGRES:
        cursor.execute("UPDATE users SET balance = balance + %s WHERE user_id=%s", (amount, user_id))
    else:
        cursor.execute("UPDATE users SET balance = balance + ? WHERE user_id=?", (amount, user_id))
    conn.commit()
