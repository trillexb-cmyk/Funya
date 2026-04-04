from database import get_user, update_balance

# ===== БАЛАНС =====
def show_balance(bot, message):
    user = get_user(message.from_user.id)

    if not user:
        bot.send_message(message.chat.id, "❌ Ты не зарегистрирован. Напиши /start")
        return

    bot.send_message(
        message.chat.id,
        f"💰 Баланс: {user[1]} 🍬 Фунтиков\n🍪 Печеньки: {user[2]}"
    )


# ===== БОНУС =====
def get_bonus(bot, message):
    update_balance(message.from_user.id, 2500)

    bot.send_message(
        message.chat.id,
        "🎁 Бонус\n\n+2500 💰"
    )


# ===== ПЕРЕВОД =====
def transfer(bot, message):
    if not message.reply_to_message:
        bot.send_message(message.chat.id, "❌ Ответь на сообщение пользователя")
        return

    try:
        args = message.text.split()
        amount = int(args[-1])
    except:
        bot.send_message(message.chat.id, "❌ Укажи сумму: фуня перевод 100")
        return

    sender_id = message.from_user.id
    target_id = message.reply_to_message.from_user.id

    user = get_user(sender_id)

    if user[1] < amount:
        bot.send_message(message.chat.id, "❌ Недостаточно средств")
        return

    # списание и начисление
    update_balance(sender_id, -amount)
    update_balance(target_id, amount)

    bot.send_message(
        message.chat.id,
        f"💸 Перевод выполнен\n{amount} 💰 отправлено"
    )
