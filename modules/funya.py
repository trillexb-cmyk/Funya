import random


# ===== ОБЫЧНЫЕ ФРАЗЫ =====
PHRASES = [
    "👀 Я тут",
    "😏 Чего звал?",
    "🤖 На связи",
    "🔥 Фуня в деле",
    "😎 Кто меня звал?",
]


# ===== ХОРОШИЕ ОТВЕТЫ =====
GOOD = [
    "😎 Конечно",
    "🔥 Ещё бы",
    "💯 Без вариантов",
    "👑 Факт",
]


# ===== ЗАЩИТА БОТА =====
BAD = [
    "😏 Мимо",
    "💀 Даже не близко",
    "👑 Попробуй ещё раз",
    "🔥 Ошибаешься",
]


# ===== ОБЫЧНЫЕ ДА/НЕТ =====
YES_NO = [
    "✅ Да",
    "❌ Нет",
    "🤔 Возможно",
    "😏 Скорее да",
    "😐 Скорее нет",
]


# ===== ПРИЗНАКИ ХОРОШЕГО / ПЛОХОГО =====
GOOD_WORDS = ["крас", "умн", "крут", "сильн", "луч", "топ"]
BAD_WORDS = ["туп", "урод", "лох", "слаб", "глуп", "ужас"]


# ===== КТО УПОМИНАЕТСЯ =====
def get_subject(text):
    words = text.split()

    if "ты" in words:
        return "bot"
    elif "я" in words:
        return "self"
    elif "он" in words:
        return "he"
    elif "она" in words:
        return "she"
    elif "они" in words:
        return "they"

    return None


# ===== ОПРЕДЕЛЕНИЕ ТОНА =====
def get_tone(text):
    for w in GOOD_WORDS:
        if w in text:
            return "good"

    for w in BAD_WORDS:
        if w in text:
            return "bad"

    return "neutral"


# ===== ОТПРАВКА =====
def send(bot, message, text):
    bot.send_message(
        message.chat.id,
        text,
        reply_to_message_id=message.message_id
    )


# ===== ГЛАВНАЯ =====
def run(bot, message, text):
    text = text.strip().lower()


    # ===== ПРОСТО ФУНЯ =====
    if text == "":
        send(bot, message, random.choice(PHRASES))
        return


    subject = get_subject(text)


    # ===== ЕСЛИ ОБРАЩЕНИЕ К БОТУ =====
    if subject == "bot":
        tone = get_tone(text)

        if tone == "good":
            send(bot, message, random.choice(GOOD))
        elif tone == "bad":
            send(bot, message, random.choice(BAD))
        else:
            send(bot, message, random.choice(YES_NO))
        return


    # ===== ДРУГИЕ =====
    if subject:
        send(bot, message, random.choice(YES_NO))
        return


    # ===== ДА / НЕТ =====
    if "да или нет" in text:
        send(bot, message, random.choice(YES_NO))
        return


    # ===== ОСТАЛЬНОЕ =====
    send(bot, message, random.choice(PHRASES))
