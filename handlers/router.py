import handlers.menu as menu
import handlers.profile as profile
import handlers.economy as economy


# ===== СТАРТ =====
def start(bot, message):
    menu.send_menu(bot, message.chat.id)


# ===== ОБРАБОТКА =====
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
        profile.show_profile(bot, message)

    elif "бонус" in text:
        economy.get_bonus(bot, message)

    elif "баланс" in text:
        economy.show_balance(bot, message)

    elif "помощь" in text:
        menu.send_help(bot, message.chat.id)

    else:
        # В чате молчим
        return
