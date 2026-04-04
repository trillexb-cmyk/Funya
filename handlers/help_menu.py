from telebot import types


# ===== ПОМОЩЬ =====
def send_help(bot, chat_id):
    markup = types.InlineKeyboardMarkup()

    markup.add(
        types.InlineKeyboardButton("📖 Команды", callback_data="cmds")
    )

    bot.send_message(
        chat_id,
        "🤖 Я Фуня\n\nВыбери, что тебя интересует 👇",
        reply_markup=markup
    )


# ===== РАЗДЕЛЫ =====
def send_commands(bot, chat_id):
    markup = types.InlineKeyboardMarkup()

    markup.row(
        types.InlineKeyboardButton("💰 Экономика", callback_data="eco"),
        types.InlineKeyboardButton("🎭 Действия", callback_data="actions")
    )

    markup.row(
        types.InlineKeyboardButton("💍 Брак", callback_data="marry"),
        types.InlineKeyboardButton("❤️ Отношения", callback_data="love")
    )

    bot.send_message(
        chat_id,
        "📖 Выбери раздел:",
        reply_markup=markup
    )


# ===== CALLBACK =====
def handle_callbacks(bot, call):

    if call.data == "cmds":
        send_commands(bot, call.message.chat.id)

    elif call.data == "eco":
        bot.send_message(
            call.message.chat.id,
            "💰 Экономика:\n\nбаланс\nбонус"
        )

    elif call.data == "actions":
        bot.send_message(
            call.message.chat.id,
            "🎭 Действия:\n\nобнять\nпоцеловать\nукусить"
        )

    elif call.data == "marry":
        bot.send_message(
            call.message.chat.id,
            "💍 Брак:\n\n🚧 В разработке"
        )

    elif call.data == "love":
        bot.send_message(
            call.message.chat.id,
            "❤️ Отношения:\n\n🚧 В разработке"
        )
