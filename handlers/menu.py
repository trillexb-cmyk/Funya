from telebot import types

# ===== ОТПРАВКА МЕНЮ =====
def send_menu(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # верх
    markup.row("👤 Профиль", "⚒ Кузня")
    markup.row("🛒 Магазин", "👥 Команды")

    # центр
    markup.row("🏆 Турниры")

    # низ
    markup.row("💬 Чаты", "👥 Кланы")
    markup.row("🎮 Игры", "🎁 Бонус")
    markup.row("📜 Политика", "📞 Связь")

    bot.send_message(chat_id, "👋 Привет, я Фуня\n\nВыбери раздел 👇", reply_markup=markup)


# ===== ОБРАБОТКА КНОПОК =====
def handle_buttons(bot, message):
    text = message.text

    if text == "👤 Профиль":
        import handlers.profile as profile
        profile.show_profile(bot, message)

    elif text == "🎁 Бонус":
        import handlers.economy as economy
        economy.get_bonus(bot, message)

    else:
        bot.send_message(message.chat.id, "🚧 Раздел в разработке")
