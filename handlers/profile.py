from database import get_user

def register_handlers(bot):
    @bot.message_handler(func=lambda m: m.text == "👤 Профиль")
    def profile_command(message):
        user = get_user(message.from_user.id)
        text = f"""👤 Твой профиль
ID: {user[0]}
Баланс: {user[1]} 🍬 Фунтиков
🍪 Печенек: {user[2]}
Характеристика: 0
Пара: {user[4] if user[4] else 'отсутствует'}
Клан: {user[3]}"""
        bot.send_message(message.chat.id, text)
