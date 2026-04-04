import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL, sslmode="require")
conn.autocommit = True
cursor = conn.cursor()


def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id BIGINT PRIMARY KEY,
        coins INTEGER DEFAULT 0,
        inventory TEXT DEFAULT '',
        relationship TEXT DEFAULT '',
        last_bonus_date TEXT DEFAULT ''
    )
    """)
