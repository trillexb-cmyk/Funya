import telebot
import time

from config import TOKEN

import handlers.profile as profile
import handlers.economy as economy
import handlers.menu as menu

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

    text = message.text
    text_low = text.lower()

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

    # фуня
    if text_low.startswith("фуня"):

        if "меню" in text_low:
            menu.send_menu(bot, message.chat.id)

        elif "профиль" in text_low:
            profile.show_profile(bot, message)

        elif "баланс" in text_low:
            economy.show_balance(bot, message)

        elif "бонус" in text_low:
            economy.get_bonus(bot, message)

        return


print("Бот запущен...")

bot.remove_webhook()

while True:
    try:
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(5)
