from telebot import types
import handlers.profile as profile
import handlers.economy as economy
import handlers.help_menu as help_menu


# ===== КЛАВИАТУРА =====
def send_menu(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("👤 Профиль", "🎁 Бонус")
    markup.row("💰 Баланс", "📚 Помощь")
    markup.row("🎭 Действия", "💑 Отношения")
    markup.row("💍 Брак", "👥 Кланы")

    bot.send_message(chat_id, "🤖 Добро пожаловать!", reply_markup=markup)


# ===== ОБРАБОТКА КНОПОК (ФИКС) =====
def handle_buttons(bot, message):
    if not message.text:
        return False

    text = message.text.lower()

    if "профиль" in text:
        profile.show_profile(bot, message)

    elif "бонус" in text:
        economy.get_bonus(bot, message)

    elif "баланс" in text:
        economy.show_balance(bot, message)

    elif "помощь" in text:
        help_menu.send_help(bot, message.chat.id)

    elif "действия" in text:
        bot.send_message(message.chat.id, "🎭 Действия\n\n🚧 В разработке")

    elif "отношения" in text:
        bot.send_message(message.chat.id, "💑 Отношения\n\n🚧 В разработке")

    elif "брак" in text:
        bot.send_message(message.chat.id, "💍 Брак\n\n🚧 В разработке")

    elif "кланы" in text:
        bot.send_message(message.chat.id, "👥 Кланы\n\n🚧 В разработке")

    else:
        return False

    return True
