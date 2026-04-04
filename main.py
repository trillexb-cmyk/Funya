import telebot
import os
import time

import handlers.profile as profile
import handlers.economy as economy
import handlers.menu as menu

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

start_time = time.time()


# ===== СТАРТ =====
@bot.message_handler(commands=['start'])
def start(msg):
    menu.send_menu(bot, msg.chat.id)


# ===== ОБЩИЙ ОБРАБОТЧИК =====
@bot.message_handler(func=lambda message: True)
def handler(message):
    if not message.text:
        return

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
            bot.send_message(
                message.chat.id,
                f"📊 Статистика:\n⏱ {uptime} сек"
            )

    # кнопки
    else:
        menu.handle_buttons(bot, message)


print("Бот запущен...")
bot.infinity_polling()
