from telebot.types import ReplyKeyboardMarkup

def menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("👤 Профиль", "💎 Баланс")
    kb.row("🎁 Бонус", "🎒 Инвентарь")
    kb.row("🛒 Магазин", "❤️ Отношения")
    return kb
