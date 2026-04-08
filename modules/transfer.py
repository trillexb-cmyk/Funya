from database import add_user, get_user, transfer_balance


def run(bot, message, text):
    user_id = message.from_user.id
    parts = text.split()

    if len(parts) < 1:
        bot.send_message(message.chat.id, "❌ Укажи сумму")
        return

    # ===== СУММА =====
    try:
        amount = int(parts[-1])
    except:
        bot.send_message(message.chat.id, "❌ Неверная сумма")
        return

    if amount <= 0:
        bot.send_message(message.chat.id, "❌ Сумма должна быть больше 0")
        return

    # ===== КОМУ =====
    target_id = None

    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id
    else:
        bot.send_message(message.chat.id, "❌ Ответь на сообщение пользователя")
        return

    if target_id == user_id:
        bot.send_message(message.chat.id, "❌ Нельзя перевести себе")
        return

    # ===== БД =====
    add_user(user_id)
    add_user(target_id)

    sender = get_user(user_id)

    if sender["balance"] < amount:
        bot.send_message(message.chat.id, "❌ Недостаточно средств")
        return

    # ===== ПЕРЕВОД =====
    transfer_balance(user_id, target_id, amount)

    bot.send_message(
        message.chat.id,
        f"💸 Перевод выполнен!\n\n"
        f"📤 Отправлено: {amount}\n"
        f"📥 Пользователю: {target_id}"
    )
