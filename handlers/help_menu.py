from telebot import types


# ===== ГЛАВНОЕ МЕНЮ =====
def send_help(bot, chat_id):
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton("💰 Экономика", callback_data="cat_economy"))
    markup.add(types.InlineKeyboardButton("🎭 Действия", callback_data="cat_actions"))
    markup.add(types.InlineKeyboardButton("💑 Отношения", callback_data="cat_love"))

    bot.send_message(
        chat_id,
        "📚 Помощь\n\nВыбери категорию:",
        reply_markup=markup
    )


# ===== CALLBACK =====
def handle_callbacks(bot, call):

    # ===== НАЗАД В ГЛАВНОЕ =====
    if call.data == "back_main":
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("💰 Экономика", callback_data="cat_economy"))
        markup.add(types.InlineKeyboardButton("🎭 Действия", callback_data="cat_actions"))
        markup.add(types.InlineKeyboardButton("💑 Отношения", callback_data="cat_love"))

        safe_edit(bot, call, "📚 Помощь\n\nВыбери категорию:", markup)
        return


    # ===== ЭКОНОМИКА (подкатегории) =====
    if call.data == "cat_economy":
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("💵 Баланс", callback_data="eco_balance"))
        markup.add(types.InlineKeyboardButton("🎁 Бонус", callback_data="eco_bonus"))
        markup.add(types.InlineKeyboardButton("🔄 Переводы", callback_data="eco_transfer"))
        markup.add(types.InlineKeyboardButton("🔙 Назад", callback_data="back_main"))

        safe_edit(bot, call, "💰 Экономика\n\nВыбери раздел:", markup)
        return


    # ===== ДЕЙСТВИЯ (подкатегории) =====
    if call.data == "cat_actions":
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("❤️ Романтика", callback_data="act_love"))
        markup.add(types.InlineKeyboardButton("😈 Агрессивные", callback_data="act_agro"))
        markup.add(types.InlineKeyboardButton("🔙 Назад", callback_data="back_main"))

        safe_edit(bot, call, "🎭 Действия\n\nВыбери тип:", markup)
        return


    # ===== ОТНОШЕНИЯ =====
    if call.data == "cat_love":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 Назад", callback_data="back_main"))

        safe_edit(bot, call, "💑 Отношения\n\n🚧 В разработке", markup)
        return


    # ===== ЭКОНОМИКА — ДЕТАЛИ =====
    if call.data == "eco_balance":
        text = "💵 Баланс\n\nКоманда:\nбаланс"
        back = "cat_economy"

    elif call.data == "eco_bonus":
        text = "🎁 Бонус\n\nКоманда:\nбонус"
        back = "cat_economy"

    elif call.data == "eco_transfer":
        text = "🔄 Переводы\n\nКоманда:\nперевод"
        back = "cat_economy"


    # ===== ДЕЙСТВИЯ — ДЕТАЛИ =====
    elif call.data == "act_love":
        text = "❤️ Романтика\n\nобнять\nпоцеловать"
        back = "cat_actions"

    elif call.data == "act_agro":
        text = "😈 Агрессивные\n\nукусить"
        back = "cat_actions"

    else:
        return


    # ===== КНОПКА НАЗАД =====
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 Назад", callback_data=back))

    safe_edit(bot, call, text, markup)


# ===== БЕЗОПАСНОЕ РЕДАКТИРОВАНИЕ =====
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
