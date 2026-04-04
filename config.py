import os

TOKEN = os.environ.get("TOKEN")  # токен бота
USE_POSTGRES = bool(os.environ.get("DATABASE_URL"))  # True если DATABASE_URL задан
TIMEZONE = os.environ.get("TIMEZONE", "Europe/Kiev")  # для бонусов
