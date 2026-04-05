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


# ===== СТАРТ =====
def start(bot, message):
    menu.send_menu(bot, message.chat.id)


# ===== ОСНОВНОЙ РОУТЕР =====
def handle(bot, message):
    if not message.text:
        return

    text = message.text
    text_low = text.lower().strip()

    print("MSG:", text_low)


    # ===== КНОПКИ (ЛС) =====
    if message.chat.type == "private":
        if menu.handle_buttons(bot, message):
            return


    # ===== БАН (ТОЛЬКО В ГРУППЕ) =====
    if text_low == "бан":
        ban.run(bot, message)
        return


    # ===== ФУНЯ =====
    if text_low.startswith("фуня"):
        cleaned = text_low.replace("фуня", "", 1).strip()
        funya.run(bot, message, cleaned)
        return


    # ===== КОМАНДЫ =====
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
