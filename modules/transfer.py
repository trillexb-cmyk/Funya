from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user, get_user, update_balance

pending_transfers = {}


def run(bot, message):
    user_id = message.from_user.id
    add_user(user_id)

    args = message.text.split()

    # ===== ОТВЕТОМ =====
    if message.reply_to_message:
        if len(args) < 2:
            bot.send_message(message.chat.id, "❌ Укажи сумму")
            return

        try:
            amount = int(args[1])
        except:
            bot.send_message(message.chat.id, "❌ Неверная сумма")
            return

        target_id = message.reply_to_message.from_user.id

    else:
        if len(args) < 3:
            bot.send_message(message.chat.id, "❌ Используй: перевод ID сумма")
            return

        target = args[1]

        try:
            amount = int(args[2])
        except:
            bot.send_message(message.chat.id, "❌ Неверная сумма")
            return

        if target.isdigit():
            target_id = int(target)
        else:
            try:
                target_id = bot.get_chat(target).id
            except:
                bot.send_message(message.chat.id, "❌ Пользователь не найден")
                return

    # ===== ПРОВЕРКИ =====
    if amount <= 0:
        bot.send_message(message.chat.id, "❌ Сумма должна быть больше 0")
        return

    if target_id == user_id:
        bot.send_message(message.chat.id, "❌ Нельзя себе")
        return

    sender = get_user(user_id)

    if sender["balance"] < amount:
        bot.send_message(message.chat.id, "❌ Недостаточно средств")
        return

    key = f"{user_id}:{target_id}"

    pending_transfers[key] = {
        "from": user_id,
        "to": target_id,
        "amount": amount
    }

    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("✅ Подтвердить", callback_data=f"pay_yes:{key}"),
        InlineKeyboardButton("❌ Отмена", callback_data=f"pay_no:{key}")
    )

    bot.send_message(
        message.chat.id,
        f"💸 Подтверди перевод\n\n"
        f"👤 Кому: {target_id}\n"
        f"💰 Сумма: {amount}",
        reply_markup=kb
    )


def callback(bot, call):
    data = call.data

    if not data.startswith("pay_"):
        return

    action, key = data.split(":")

    if key not in pending_transfers:
        bot.answer_callback_query(call.id, "❌ Перевод не найден")
        return

    transfer = pending_transfers[key]

    if call.from_user.id != transfer["from"]:
        bot.answer_callback_query(call.id, "❌ Это не твой перевод")
        return

    if action == "pay_no":
        del pending_transfers[key]
        bot.edit_message_text("❌ Перевод отменён", call.message.chat.id, call.message.message_id)
        return

    sender = get_user(transfer["from"])

    if sender["balance"] < transfer["amount"]:
        bot.edit_message_text("❌ Недостаточно средств", call.message.chat.id, call.message.message_id)
        return

    update_balance(transfer["from"], -transfer["amount"])
    update_balance(transfer["to"], transfer["amount"])

    bot.edit_message_text(
        f"✅ Перевод выполнен!\n\n💰 {transfer['amount']}",
        call.message.chat.id,
        call.message.message_id
    )

    # уведомление получателю
    try:
        bot.send_message(
            transfer["to"],
            f"💸 Тебе перевели!\n\n💰 +{transfer['amount']}"
        )
    except:
        pass

    del pending_transfers[key]
