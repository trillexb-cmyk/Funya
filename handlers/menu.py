from telebot import types


# ===== МЕНЮ (ЛС) =====
def send_menu(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("👤 Профиль", "🎁 Бонус")

    markup.row("⚒ Кузня", "🛒 Магазин")
    markup.row("👥 Команды", "🏆 Турниры")

    markup.row("💬 Чаты", "👥 Кланы")
    markup.row("🎮 Игры")

    markup.row("📜 Политика", "📞 Связь")

    bot.send_message(chat_id, "📋 Меню", reply_markup=markup)


# ===== ОБРАБОТКА КНОПОК =====
def handle_buttons(bot, message):
    text = message.text

    # ===== РАБОЧИЕ =====
    if text == "👤 Профиль":
        from handlers.profile import show_profile
        show_profile(bot, message)

    elif text == "🎁 Бонус":
        from handlers.economy import get_bonus
        get_bonus(bot, message)

    # ===== ЗАГЛУШКИ =====
    elif text in [
        "⚒ Кузня", "🛒 Магазин", "👥 Команды",
        "🏆 Турниры",
        "💬 Чаты", "👥 Кланы",
        "🎮 Игры",
        "📜 Политика", "📞 Связь"
    ]:
        bot.send_message(message.chat.id, "🚧 Раздел в разработке")
