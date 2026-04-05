from telebot import types


# ===== ГЛАВНОЕ МЕНЮ =====
def send_help(bot, chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("💰 Экономика", callback_data="help_economy"),
        types.InlineKeyboardButton("🎭 Действия", callback_data="help_actions"),
    )
    markup.add(
        types.InlineKeyboardButton("💑 Отношения", callback_data="help_love"),
        types.InlineKeyboardButton("💍 Брак", callback_data="help_marriage"),
    )
    markup.add(
        types.InlineKeyboardButton("👥 Кланы", callback_data="help_clans"),
    )

    bot.send_message(
        chat_id,
        "📚 Помощь\n\nВыбери раздел:",
        reply_markup=markup
    )


# ===== CALLBACK =====
def handle_callbacks(bot, call):

    # ===== НАЗАД =====
    if call.data == "help_back":
        send_help_edit(bot, call)
        bot.answer_callback_query(call.id)
        return


    # ===== РАЗДЕЛЫ =====
    if call.data == "help_economy":
        text = (
            "💰 Экономика\n\n"
            "баланс — посмотреть баланс\n"
            "бонус — ежедневная награда\n"
            "перевод — отправить деньги"
        )

    elif call.data == "help_actions":
        text = "🎭 Действия\n\n🚧 В разработке"

    elif call.data == "help_love":
        text = "💑 Отношения\n\n🚧 В разработке"

    elif call.data == "help_marriage":
        text = "💍 Брак\n\n🚧 В разработке"

    elif call.data == "help_clans":
        text = "👥 Кланы\n\n🚧 В разработке"

    else:
        bot.answer_callback_query(call.id)
        return


    # ===== КНОПКА НАЗАД =====
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 Назад", callback_data="help_back"))

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

    bot.answer_callback_query(call.id)


# ===== РЕДАКТИРОВАНИЕ ГЛАВНОГО МЕНЮ =====
def send_help_edit(bot, call):
    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("💰 Экономика", callback_data="help_economy"),
        types.InlineKeyboardButton("🎭 Действия", callback_data="help_actions"),
    )
    markup.add(
        types.InlineKeyboardButton("💑 Отношения", callback_data="help_love"),
        types.InlineKeyboardButton("💍 Брак", callback_data="help_marriage"),
    )
    markup.add(
        types.InlineKeyboardButton("👥 Кланы", callback_data="help_clans"),
    )

    bot.edit_message_text(
        "📚 Помощь\n\nВыбери раздел:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )
