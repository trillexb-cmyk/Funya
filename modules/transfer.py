from handlers import menu

from modules import profile
from modules import bonus
from modules import balance
from modules import help as help_cmd
from modules import actions
from modules import relations
from modules import marriage
from modules import clans
from modules import funya
from modules import ban
from modules import transfer  # 🔥 добавили


def start(bot, message):
    menu.send_menu(bot, message.chat.id)


def handle(bot, message):
    if not message.text:
        return

    text = message.text
    text_low = text.lower().strip()

    print("MSG:", text_low)

    # ===== КНОПКИ =====
    if message.chat.type == "private":
        if menu.handle_buttons(bot, message):
            return

    # ===== БАН =====
    if text_low == "бан":
        ban.run(bot, message)
        return

    # ===== ФУНЯ =====
    if text_low.startswith("фуня"):
        cleaned = text_low.replace("фуня", "", 1).strip()
        funya.run(bot, message, cleaned)
        return

    # ===== 💸 ПЕРЕВОД =====
    if text_low == "п" or text_low.startswith(("перевести", "перевод", "п ")):
        args = text_low.split()

        if len(args) < 2:
            bot.send_message(message.chat.id, "❌ Используй: перевести <сумма> [ID] или ответом")
            return

        # сумма
        try:
            amount = int(args[1])
        except:
            bot.send_message(message.chat.id, "❌ Сумма должна быть числом")
            return

        from_id = message.from_user.id
        from_name = message.from_user.first_name

        to_id = None
        to_name = "пользователь"

        # 🔹 1. Ответ на сообщение
        if message.reply_to_message:
            target_user = message.reply_to_message.from_user
            to_id = target_user.id
            to_name = target_user.first_name

        # 🔹 2. Через ID
        elif len(args) >= 3:
            target = args[2]

            if target.isdigit():
                to_id = int(target)
            else:
                bot.send_message(message.chat.id, "❌ Укажи корректный ID или ответь на сообщение")
                return

        else:
            bot.send_message(message.chat.id, "❌ Укажи получателя или ответь на сообщение")
            return

        success, text = transfer.transfer_balance(from_id, to_id, amount)

        if success:
            # ответ отправителю
            bot.send_message(
                message.chat.id,
                f"💸 Ты перевел {amount} монет пользователю {to_name}"
            )

            # уведомление получателю
            try:
                bot.send_message(
                    to_id,
                    f"💰 Тебе перевели {amount} монет!\n👤 От: {from_name}"
                )
            except:
                pass
        else:
            bot.send_message(message.chat.id, text)

        return

    # ===== ОБЫЧНЫЕ КОМАНДЫ =====
    if "профиль" in text_low:
        profile.run(bot, message)

    elif "бонус" in text_low:
        bonus.run(bot, message)

    elif "баланс" in text_low:
        balance.run(bot, message)

    elif "помощь" in text_low:
        help_cmd.run(bot, message)

    elif "действия" in text_low:
        actions.run(bot, message)

    elif "отношения" in text_low:
        relations.run(bot, message)

    elif "брак" in text_low:
        marriage.run(bot, message)

    elif "кланы" in text_low:
        clans.run(bot, message)

    else:
        return
