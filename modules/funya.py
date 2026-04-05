import random


PHRASES = [
    "👀 Я тут",
    "😏 Чего звал?",
    "🤖 На связи",
    "🔥 Фуня в деле"
]


YES_NO = [
    "✅ Да",
    "❌ Нет",
    "🤔 Скорее да",
    "😐 Скорее нет"
]


WHO_AM_I = [
    "🤡 Ты долбаёб",
    "😏 шлюха",
    "🔥 соска",
    "💀 Урод",
    "🧠 Попробую ещё раз подумать",
]


def run(bot, message, text):
    text = text.strip()


    # ===== ПРОСТО ФУНЯ =====
    if text == "":
        bot.send_message(message.chat.id, random.choice(PHRASES))
        return


    # ===== КТО Я =====
    if "кто я" in text:
        bot.send_message(message.chat.id, random.choice(WHO_AM_I))
        return


    # ===== ДА / НЕТ =====
    if "да или нет" in text:
        bot.send_message(message.chat.id, random.choice(YES_NO))
        return


    # ===== НЕ ПОНЯЛ =====
    bot.send_message(message.chat.id, "🤖 Не понял вопрос")
