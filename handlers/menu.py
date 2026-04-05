from telebot import types


def send_menu(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("👤 Профиль", "🎁 Бонус")
    markup.row("💰 Баланс", "📚 Помощь")
    markup.row("🎭 Действия", "💑 Отношения")
    markup.row("💍 Брак", "👥 Кланы")

    bot.send_message(chat_id, "🤖 Панель управления", reply_markup=markup)


def handle_buttons(bot, message):
    text = message.text.lower()

    if "профиль" in text:
        from modules import profile
        profile.run(bot, message)
        return True

    elif "бонус" in text:
        from modules import bonus
        bonus.run(bot, message)
        return True

    elif "баланс" in text:
        from modules import balance
        balance.run(bot, message)
        return True

    elif "помощь" in text:
        from modules import help as help_cmd
        help_cmd.run(bot, message)
        return True

    elif "действия" in text:
        from modules import actions
        actions.run(bot, message)
        return True

    elif "отношения" in text:
        from modules import relations
        relations.run(bot, message)
        return True

    elif "брак" in text:
        from modules import marriage
        marriage.run(bot, message)
        return True

    elif "кланы" in text:
        from modules import clans
        clans.run(bot, message)
        return True

    return False
