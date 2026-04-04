from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def help_main():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("💎 Экономика", callback_data="help_economy"),
        InlineKeyboardButton("🎭 Действия", callback_data="help_actions")
    )
    kb.add(
        InlineKeyboardButton("👤 Профиль", callback_data="help_profile"),
        InlineKeyboardButton("🤖 Прочее", callback_data="help_other")
    )
    return kb

def back():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⬅️ Назад", callback_data="help_back"))
    return kb
