import handlers.menu as menu
import handlers.profile as profile
import handlers.economy as economy


def handle_all(bot, message):
    if not message.text:
        print("❌ Нет текста")
        return False

    text = message.text
    text_low = text.lower()

    print("\n====== NEW MESSAGE ======")
    print("TEXT:", text)
    print("CHAT TYPE:", message.chat.type)

    # ===== КНОПКИ =====
    if message.chat.type == "private":
        print("➡️ Проверка кнопок...")

        if menu.handle_buttons(bot, message):
            print("✅ Кнопка обработана")
            return True
        else:
            print("❌ Не кнопка")

    # ===== ФУНЯ =====
    if "фуня" in text_low:
        print("➡️ Обнаружено слово: фуня")

        clean = text_low.replace("фуня", "").strip()

        if clean == "":
            bot.send_message(message.chat.id, "👀 Я тут")
            print("✅ Ответ на фуня")
            return True

        if "профиль" in clean:
            profile.show_profile(bot, message)
            print("✅ Профиль через фуня")
            return True

        if "бонус" in clean:
            economy.get_bonus(bot, message)
            print("✅ Бонус через фуня")
            return True

        print("❌ Неизвестная команда после фуня")
        return True

    print("❌ Сообщение проигнорировано")
    return False
