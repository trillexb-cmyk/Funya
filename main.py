import telebot
import time
import random

from config import TOKEN

import handlers.profile as profile
import handlers.economy as economy
import handlers.menu as menu
import handlers.help_menu as help_menu

bot = telebot.TeleBot(TOKEN)

start_time = time.time()


# ===== СТАРТ =====
@bot.message_handler(commands=['start'])
def start(msg):
    if msg.chat.type == "private":
        menu.send_menu(bot, msg.chat.id)


# ===== CALLBACK КНОПКИ =====
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

    # =========================
    # 🔹 ЛС
    # =========================
    if message.chat.type == "private":

        # кнопки
        if text in [
            "👤 Профиль", "🎁 Бонус",
            "⚒ Кузня", "🛒 Магазин", "👥 Команды",
            "🏆 Турниры",
            "💬 Чаты", "👥 Кланы",
            "🎮 Игры",
            "📜 Политика", "📞 Связь"
        ]:
            menu.handle_buttons(bot, message)
            return

        # команды
        if "профиль" in text_low:
            profile.show_profile(bot, message)

        elif "баланс" in text_low:
            economy.show_balance(bot, message)

        elif "бонус" in text_low:
            economy.get_bonus(bot, message)

        elif "помощь" in text_low:
            help_menu.send_help(bot, message.chat.id)

        elif "команды" in text_low:
            help_menu.send_commands(bot, message.chat.id)

        return


    # =========================
    # 🔹 ЧАТЫ
    # =========================
    else:

        original_text = text_low

        # реакция на "фуня"
        if text_low.startswith("фуня"):
            text_low = text_low.replace("фуня", "").strip()

        # просто "фуня"
        if original_text.strip() == "фуня":
            phrases = [
                "👀 Я тут",
                "😏 Чего звал?",
                "🤖 На связи",
                "🔥 Фуня в деле",
                "😎 Слушаю тебя",
                "💭 Что нужно?",
                "⚡ Быстро говори"
            ]
            bot.send_message(message.chat.id, random.choice(phrases))
            return

        # команды
        if "профиль" in text_low:
            profile.show_profile(bot, message)

        elif "баланс" in text_low:
            economy.show_balance(bot, message)

        elif "бонус" in text_low:
            economy.get_bonus(bot, message)

        elif "помощь" in text_low:
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
