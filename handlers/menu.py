from telebot import types


# ===== КЛАВИАТУРА =====
def send_menu(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("👤 Профиль", "🎁 Бонус")
    markup.row("💰 Баланс", "📚 Помощь")

    bot.send_message(chat_id, "🤖 Панель управления", reply_markup=markup)


# ===== КНОПКИ =====
def handle_buttons(bot, message):
    text = message.text.lower()

    if "профиль" in text:
        from handlers.profile import show_profile
        show_profile(bot, message)
        return True

    elif "бонус" in text:
        from handlers.economy import get_bonus
        get_bonus(bot, message)
        return True

    elif "баланс" in text:
        from handlers.economy import show_balance
        show_balance(bot, message)
        return True

    elif "помощь" in text:
        send_help(bot, message.chat.id)
        return True

    return False


# ===== ПОМОЩЬ =====
def send_help(bot, chat_id):
    bot.send_message(
        chat_id,
        "📚 Помощь\n\n"
        "👤 профиль\n"
        "🎁 бонус\n"
        "💰 баланс\n"
    )
