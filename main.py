import telebot
import os
import time

from database import init_db

# подключаем модули
from handlers import profile, economy, menu

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

start_time = time.time()

# инициализация БД
init_db()


# ===== СТАРТ =====
@bot.message_handler(commands=['start'])
def start(msg):
    menu.send_menu(bot, msg.chat.id)


# ===== ОБЩИЙ ОБРАБОТЧИК =====
@bot.message_handler(func=lambda message: True)
def handler(message):
    text = message.text.lower()

    # вызов бота
    if "фуня" in text:
        if "меню" in text:
            menu.send_menu(bot, message.chat.id)

        elif "профиль" in text:
            profile.show_profile(bot, message)

        elif "баланс" in text:
            economy.show_balance(bot, message)

        elif "бонус" in text:
            economy.get_bonus(bot, message)

        elif "перевод" in text:
            economy.transfer(bot, message)

        else:
            uptime = int(time.time() - start_time)
            bot.send_message(message.chat.id,
                             f"📊 Статистика:\n⏱ {uptime} сек")

    # кнопки
    else:
        menu.handle_buttons(bot, message)


print("Бот запущен...")
bot.infinity_polling()
