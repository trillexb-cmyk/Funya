from loader import bot
from keyboards.private_menu_kb import menu
from services.user_service import *

@bot.message_handler(func=lambda m: m.chat.type == "private")
def private(m):
    text = m.text

    if text == "/start":
        bot.send_message(m.chat.id, "👋 Меню", reply_markup=menu())

    elif text == "👤 Профиль":
        uid = m.from_user.id
        bot.send_message(m.chat.id, f"💎 {get_balance(uid)}")

    elif text == "💎 Баланс":
        bot.send_message(m.chat.id, f"💎 {get_balance(m.from_user.id)}")

    elif text == "🎁 Бонус":
        if can_bonus(m.from_user.id):
            give_bonus(m.from_user.id)
            bot.send_message(m.chat.id, "🎁 +2500")
        else:
            bot.send_message(m.chat.id, "⛔ Уже получал")

    else:
        bot.send_message(m.chat.id, "🚧 Раздел в разработке")
