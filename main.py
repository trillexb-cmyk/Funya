import telebot
import time

from config import TOKEN
import handlers.router as router

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    router.start(bot, message)


@bot.message_handler(func=lambda message: True)
def handler(message):
    router.handle(bot, message)


print("Бот запущен...")

bot.remove_webhook()

while True:
    try:
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(3)
