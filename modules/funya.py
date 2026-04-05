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
    "🤔 Возможно",
    "😏 Скорее да",
    "😐 Скорее нет",
    "🔥 Однозначно да",
    "💀 Даже не думай"
]


def is_question(text):
    keywords = ["я", "он", "она", "они"]

    return (
        "?" in text and
        any(word in text for word in keywords)
    )


def send(bot, message, text):
    bot.send_message(
        message.chat.id,
        text,
        reply_to_message_id=message.message_id  # 🔥 ОТВЕТ НА СООБЩЕНИЕ
    )


def run(bot, message, text):
    text = text.strip().lower()


    # ===== ПРОСТО ФУНЯ =====
    if text == "":
        send(bot, message, random.choice(PHRASES))
        return


    # ===== ВОПРОСЫ =====
    if is_question(text):
        send(bot, message, random.choice(YES_NO))
        return


    # ===== ДА / НЕТ =====
    if "да или нет" in text:
        send(bot, message, random.choice(YES_NO))
        return


    # ===== НЕ ПОНЯЛ =====
    send(bot, message, "🤖 Не понял вопрос")
