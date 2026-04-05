from telebot import types
import handlers.profile as profile
import handlers.economy as economy


# ===== КЛАВИАТУРА =====
def send_menu(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("👤 Профиль", "🎁 Бонус")
    markup.row("💰 Баланс", "📚 Помощь")
    markup.row("🎭 Действия", "💑 Отношения")
    markup.row("💍 Брак", "👥 Кланы")

    bot.send_message(chat_id, "🤖 Меню", reply_markup=markup)


# ===== ОБРАБОТКА КНОПОК =====
def handle_buttons(bot, message):
    if not message.text:
        return False

    text = message.text.lower()

    print("BTN:", text)


    if "профиль" in text:
        profile.show_profile(bot, message)
        return True

    if "бонус" in text:
        economy.get_bonus(bot, message)
        return True

    if any(word in text for word in [
        "баланс",
        "помощь",
        "действия",
        "отношения",
        "брак",
        "кланы"
    ]):
        bot.send_message(message.chat.id, "🚧 Раздел в разработке")
        return True

    return False
