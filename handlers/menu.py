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


# ===== НОРМАЛИЗАЦИЯ ТЕКСТА =====
def normalize(text: str):
    return text.lower().replace(" ", "")


# ===== ОБРАБОТКА КНОПОК =====
def handle_buttons(bot, message):
    if not message.text:
        return False

    raw = message.text
    text = normalize(raw)

    print("BTN:", raw)  # 👈 дебаг

    if text == "👤профиль" or text == "профиль":
        profile.show_profile(bot, message)

    elif text == "🎁бонус" or text == "бонус":
        economy.get_bonus(bot, message)

    elif text == "💰баланс" or text == "баланс":
        economy.show_balance(bot, message)

    elif text == "📚помощь" or text == "помощь":
        help_menu.send_help(bot, message.chat.id)

    elif text == "🎭действия" or text == "действия":
        bot.send_message(message.chat.id, "🎭 Действия\n\n🚧 В разработке")

    elif text == "💑отношения" or text == "отношения":
        bot.send_message(message.chat.id, "💑 Отношения\n\n🚧 В разработке")

    elif text == "💍брак" or text == "брак":
        bot.send_message(message.chat.id, "💍 Брак\n\n🚧 В разработке")

    elif text == "👥кланы" or text == "кланы":
        bot.send_message(message.chat.id, "👥 Кланы\n\n🚧 В разработке")

    else:
        return False

    return True
