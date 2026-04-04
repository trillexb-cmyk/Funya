from telebot import types
import handlers.profile as profile
import handlers.economy as economy

# ===== МЕНЮ =====
def send_menu(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("👤 Профиль", "⚒ Кузня")
    markup.row("🛒 Магазин", "👥 Команды")
    markup.row("🏆 Турниры")
    markup.row("💬 Чаты", "👥 Кланы")
    markup.row("🎮 Игры", "🎁 Бонус")
    markup.row("📜 Политика", "📞 Связь")

    bot.send_message(chat_id, "👋 Привет, я Фуня\n\nВыбери раздел 👇", reply_markup=markup)


# ===== КНОПКИ =====
def handle_buttons(bot, message):
    text = message.text

    if text == "👤 Профиль":
        profile.show_profile(bot, message)

    elif text == "🎁 Бонус":
        economy.get_bonus(bot, message)

    elif text in [
        "⚒ Кузня", "🛒 Магазин", "👥 Команды",
        "🏆 Турниры",
        "💬 Чаты", "👥 Кланы",
        "🎮 Игры",
        "📜 Политика", "📞 Связь"
    ]:
        bot.send_message(message.chat.id, "🚧 Раздел в разработке")
