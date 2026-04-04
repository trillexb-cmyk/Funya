import telebot
from telebot import types
import os
import time

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

start_time = time.time()


# ===== КНОПКА МЕНЮ =====
def get_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("👤 Профиль", "🛒 Магазин")
    kb.row("🎒 Инвентарь", "❤️ Отношения")
    kb.row("💰 Баланс", "🎁 Бонус")
    kb.row("📖 Помощь")
    return kb


# ===== СТАРТ =====
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "Привет 👋 Напиши 'фуня меню' чтобы открыть меню",
        reply_markup=get_menu()
    )


# ===== ОСНОВНОЙ ОБРАБОТЧИК =====
@bot.message_handler(func=lambda message: True)
def handler(message):
    text = message.text.lower()

    # ===== ВЫЗОВ БОТА =====
    if "фуня" in text:

        # меню
        if "меню" in text:
            bot.send_message(message.chat.id, "📋 Главное меню:", reply_markup=get_menu())

        # команды
        elif "команды" in text or "помощь" in text:
            bot.send_message(message.chat.id,
                             "📖 Разделы:\n"
                             "💰 Экономика\n"
                             "🎮 Действия\n"
                             "👤 Профиль\n"
                             "\n(часть в разработке)")

        # статистика
        else:
            uptime = int(time.time() - start_time)
            bot.send_message(message.chat.id,
                             f"📊 Статистика:\n"
                             f"⏱ Время работы: {uptime} сек\n"
                             f"⚡ Пинг: OK\n")

    # ===== КНОПКИ =====
    elif text == "👤 профиль":
        bot.send_message(message.chat.id, "👤 Профиль в разработке")

    elif text == "🛒 магазин":
        bot.send_message(message.chat.id, "🛒 Магазин в разработке")

    elif text == "🎒 инвентарь":
        bot.send_message(message.chat.id, "🎒 Инвентарь в разработке")

    elif text == "❤️ отношения":
        bot.send_message(message.chat.id, "❤️ Отношения в разработке")

    elif text == "💰 баланс":
        bot.send_message(message.chat.id, "💰 Баланс в разработке")

    elif text == "🎁 бонус":
        bot.send_message(message.chat.id, "🎁 Бонус в разработке")

    elif text == "📖 помощь":
        bot.send_message(message.chat.id,
                         "📖 Помощь:\n"
                         "Напиши: фуня меню\n"
                         "или фуня команды")


# ===== ЗАПУСК =====
print("Бот запущен...")
bot.infinity_polling()
