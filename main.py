import telebot
import time
import random

from config import TOKEN, ADMIN_ID

import handlers.menu as menu
import handlers.router as router

from database import reset_db

bot = telebot.TeleBot(TOKEN)


# ===== СТАРТ =====
@bot.message_handler(commands=['start'])
def start(msg):
    menu.send_menu(bot, msg.chat.id)


# ===== ОБЩИЙ ОБРАБОТЧИК =====
@bot.message_handler(func=lambda message: True)
def handler(message):
    router.handle_all(bot, message)


print("Бот запущен...")


# ===== ФИКС 409 =====
bot.remove_webhook()


# ===== ЗАПУСК =====
while True:
    try:
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(5)
