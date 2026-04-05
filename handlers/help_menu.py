from telebot import types


# ===== ПОМОЩЬ =====
def send_help(bot, chat_id):
    markup = types.InlineKeyboardMarkup()

    # 2 кнопки в ряд
    markup.row(
        types.InlineKeyboardButton("💰 Экономика", callback_data="cat_economy"),
        types.InlineKeyboardButton("🎭 Действия", callback_data="cat_actions")
    )

    markup.row(
        types.InlineKeyboardButton("💑 Отношения", callback_data="cat_love"),
        types.InlineKeyboardButton("💍 Брак", callback_data="cat_marriage")
    )

    markup.row(
        types.InlineKeyboardButton("👥 Кланы", callback_data="cat_clans")
    )

    bot.send_message(
        chat_id,
        "🤖 Фуня на связи!\n\n"
        "Я помогу тебе разобраться 👇\n\n"
        "Выбирай раздел:",
        reply_markup=markup
    )


# ===== CALLBACK =====
def handle_callbacks(bot, call):

    # ===== НАЗАД =====
    if call.data == "back_main":
        markup = types.InlineKeyboardMarkup()

        markup.row(
            types.InlineKeyboardButton("💰 Экономика", callback_data="cat_economy"),
            types.InlineKeyboardButton("🎭 Действия", callback_data="cat_actions")
        )

        markup.row(
            types.InlineKeyboardButton("💑 Отношения", callback_data="cat_love"),
            types.InlineKeyboardButton("💍 Брак", callback_data="cat_marriage")
        )

        markup.row(
            types.InlineKeyboardButton("👥 Кланы", callback_data="cat_clans")
        )

        safe_edit(
            bot,
            call,
            "🤖 Фуня снова тут 😏\n\nВыбирай раздел 👇",
            markup
        )
        return


    # ===== ЭКОНОМИКА =====
    if call.data == "cat_economy":
        text = (
            "💰 Ну что, к деньгам? 😏\n\n"
            "💵 баланс — узнать сколько у тебя\n"
            "🎁 бонус — забрать награду\n"
            "🔄 перевод — отправить деньги"
        )

    # ===== ДЕЙСТВИЯ =====
    elif call.data == "cat_actions":
        text = (
            "🎭 Пора действовать 😏\n\n"
            "❤️ обнять\n"
            "💋 поцеловать\n"
            "😈 укусить"
        )

    # ===== ОТНОШЕНИЯ =====
    elif call.data == "cat_love":
        text = (
            "💑 Отношения\n\n"
            "🚧 В разработке"
        )

    # ===== БРАК =====
    elif call.data == "cat_marriage":
        text = (
            "💍 Брак\n\n"
            "скоро здесь можно будет:\n"
            "— делать предложение 💍\n"
            "— принимать 💖\n"
            "— разводиться 😢"
        )

    # ===== КЛАНЫ =====
    elif call.data == "cat_clans":
        text = (
            "👥 Кланы\n\n"
            "скоро появится:\n"
            "— создание клана\n"
            "— вступление\n"
            "— управление"
        )

    else:
        return


    # ===== КНОПКА НАЗАД =====
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data="back_main"))

    safe_edit(bot, call, text, markup)


# ===== SAFE EDIT =====
def safe_edit(bot, call, text, markup):
    try:
        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    except:
        pass

    bot.answer_callback_query(call.id)
