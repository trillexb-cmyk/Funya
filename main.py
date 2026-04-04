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


# ===== CALLBACK =====
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

    print("TEXT:", text)  # DEBUG

    # ===== РЕСЕТ БД =====
    if text_low == "ресет":
        if message.from_user.id == ADMIN_ID:
            reset_db()
            bot.send_message(message.chat.id, "✅ База данных очищена")
        else:
            bot.send_message(message.chat.id, "❌ Нет доступа")
        return

    # ===== КНОПКИ (ЖЁСТКИЙ ФИКС) =====
    if text in ["👤 Профиль", "🎁 Бонус"]:
        menu.handle_buttons(bot, message)
        return

    # ===== УБИРАЕМ "ФУНЯ" =====
    if text_low.startswith("фуня"):
        text_low = text_low.replace("фуня", "").strip()

    # ===== ПРОСТО "ФУНЯ" =====
    if text_low == "фуня":
        phrases = [
            "👀 Я тут",
            "😏 Чего звал?",
            "🤖 На связи",
            "🔥 Фуня в деле"
        ]
        bot.send_message(message.chat.id, random.choice(phrases))
        return

    # ===== КОМАНДЫ (ФИКС КНОПОК) =====
    if text_low in ["профиль", "👤 профиль"]:
        profile.show_profile(bot, message)

    elif text_low in ["баланс"]:
        economy.show_balance(bot, message)

    elif text_low in ["бонус", "🎁 бонус"]:
        economy.get_bonus(bot, message)

    elif "помощь" in text_low:
        help_menu.send_help(bot, message.chat.id)

    elif "команды" in text_low:
        help_menu.send_commands(bot, message.chat.id)

    else:
        return


print("Бот запущен...")

# фикс 409 ошибки
bot.remove_webhook()

while True:
    try:
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(5)        elif "помощь" in text_low:
            help_menu.send_help(bot, message.chat.id)

        elif "команды" in text_low:
            help_menu.send_commands(bot, message.chat.id)

        else:
            return


print("Бот запущен...")

bot.remove_webhook()

while True:
    try:
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(5)
