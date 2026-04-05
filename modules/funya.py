import random
from modules import help as help_cmd
from modules import profile, bonus, balance


# ===== ФРАЗЫ =====
PHRASES = [
    "👀 Я тут",
    "😏 Чего звал?",
    "🤖 На связи",
    "🔥 Фуня в деле",
    "😎 Кто меня звал?",
]


# ===== ОТПРАВКА (ВСЕГДА REPLY) =====
def send(bot, message, text):
    bot.send_message(
        message.chat.id,
        text,
        reply_to_message_id=message.message_id
    )


# ===== ГЛАВНАЯ =====
def run(bot, message, text):
    text = text.strip().lower()


    # ===== ПРОСТО "ФУНЯ" =====
    if text == "":
        send(bot, message, random.choice(PHRASES))
        return True


    # ===== КОМАНДЫ ЧЕРЕЗ ФУНЮ =====
    if "помощь" in text or "помоги" in text:
        help_cmd.run(bot, message)
        return True

    if "профиль" in text:
        profile.run(bot, message)
        return True

    if "бонус" in text:
        bonus.run(bot, message)
        return True

    if "баланс" in text:
        balance.run(bot, message)
        return True


    # ===== ЕСЛИ НЕ ПОНЯЛ — ОТВЕЧАЕТ =====
    send(bot, message, random.choice(PHRASES))
    return True
