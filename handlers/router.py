from handlers import menu

from modules import profile
from modules import bonus
from modules import balance
from modules import help as help_cmd
from modules import actions
from modules import relations
from modules import marriage
from modules import clans


def start(bot, message):
    menu.send_menu(bot, message.chat.id)


def handle(bot, message):
    if not message.text:
        return

    text = message.text.lower()

    print("MSG:", text)


    # ===== КНОПКИ (ЛС) =====
    if message.chat.type == "private":
        if menu.handle_buttons(bot, message):
            return


    # ===== УБИРАЕМ "ФУНЯ" =====
    if text.startswith("фуня"):
        text = text.replace("фуня", "", 1).strip()


    # ===== КОМАНДЫ =====
    if "профиль" in text:
        profile.run(bot, message)

    elif "бонус" in text:
        bonus.run(bot, message)

    elif "баланс" in text:
        balance.run(bot, message)

    elif "помощь" in text:
        help_cmd.run(bot, message)

    elif "действия" in text:
        actions.run(bot, message)

    elif "отношения" in text:
        relations.run(bot, message)

    elif "брак" in text:
        marriage.run(bot, message)

    elif "кланы" in text:
        clans.run(bot, message)

    else:
        return
