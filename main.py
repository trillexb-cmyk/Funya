import telebot
import time
import random

from config import TOKEN, ADMIN_ID

import handlers.profile as profile
import handlers.economy as economy
import handlers.menu as menu
import handlers.help_menu as help_menu

from database import reset_db

bot = telebot.TeleBot(TOKEN)


# ===== СТАРТ =====
@bot.message_handler(commands=['start'])
def start(msg):
    if msg.chat.type == "private":
        menu.send_menu(bot, msg.chat.id)


# ===== CALLBACK (кнопки помощи) =====
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    help_menu.handle_callbacks(bot, call)


# ===== ОБЩИЙ ОБРАБОТЧИК =====
@bot.message_handler(func=lambda message: True)
def handler(message):
    if not message.text:
        return

    text = message.text
    text_low = text.lower()

    print("TEXT:", text)


    # ===== РЕСЕТ БД =====
    if text_low == "ресет":
        if message.from_user.id == ADMIN_ID:
            reset_db()
            bot.send_message(message.chat.id, "✅ База данных очищена")
        else:
            bot.send_message(message.chat.id, "❌ Нет доступа")
        return


    # ===== КНОПКИ =====
    if text == "👤 Профиль":
        profile.show_profile(bot, message)
        return

    if text == "🎁 Бонус":
        economy.get_bonus(bot, message)
        return


    # ===== ФУНЯ =====
    if text_low == "фуня":
        phrases = [
            "👀 Я тут",
            "😏 Чего звал?",
            "🤖 На связи",
            "🔥 Фуня в деле"
        ]
        bot.send_message(message.chat.id, random.choice(phrases))
        return

    if text_low.startswith("фуня "):
        text_low = text_low.replace("фуня ", "", 1)


    # ===== КОМАНДЫ =====
    if "профиль" in text_low:
        profile.show_profile(bot, message)

    elif "баланс" in text_low:
        economy.show_balance(bot, message)

    elif "бонус" in text_low:
        economy.get_bonus(bot, message)

    elif "помощь" in text_low:
        help_menu.send_help(bot, message.chat.id)

    else:
        return  # игнор


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
