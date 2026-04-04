from telebot import types
from database import add_user

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_command(message):
        add_user(message.from_user.id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("👤 Профиль", "⚒ Кузня")
        markup.row("🛒 Магазин", "👥 Команды")
        markup.row("💬 Чаты", "👥 Кланы")
        markup.row("🎮 Игры", "🎁 Бонус")
        markup.row("📜 Политика", "📞 Связь")
        markup.row("🏆 Турниры")
        bot.send_message(message.chat.id,
                         "👋 Привет, я Фуня! Выбери раздел 👇",
                         reply_markup=markup)
