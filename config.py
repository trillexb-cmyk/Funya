import os

# токен бота (из Railway / .env)
TOKEN = os.environ.get("TOKEN")

# если есть DATABASE_URL → используем Postgres
USE_POSTGRES = bool(os.environ.get("DATABASE_URL"))

# таймзона (для бонусов)
TIMEZONE = os.environ.get("TIMEZONE", "Europe/Kiev")

# админ (обязательно поставь свой ID)
ADMIN_ID = int(os.environ.get("ADMIN_ID", "123456789"))
