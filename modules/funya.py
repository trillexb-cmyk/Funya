import random


# ===== ОБЫЧНЫЕ ФРАЗЫ =====
PHRASES = [
    "👀 Я тут",
    "😏 Чего звал?",
    "🤖 На связи",
    "🔥 Фуня в деле",
    "😎 Кто меня звал?",
]


# ===== ДА / НЕТ =====
YES_NO = [
    "✅ Да",
    "❌ Нет",
    "🤔 Возможно",
    "😏 Скорее да",
    "😐 Скорее нет",
    "🔥 Однозначно да",
    "💀 Даже не думай"
]


# ===== ПРОВЕРКА НА "Я УРОД" И Т.П. =====
def is_question(text):
    subjects = ["я", "он", "она", "они"]

    words = text.split()

    # есть ли субъект
    has_subject = any(word in words for word in subjects)

    # проверка прилагательных по окончаниям
    def is_adj(word):
        endings = (
            "ый", "ой", "ий",
            "ая", "яя",
            "ое", "ее",
            "ые", "ие"
        )
        return word.endswith(endings)

    has_adj = any(is_adj(word) for word in words)

    return has_subject and has_adj


# ===== ОТПРАВКА С ОТВЕТОМ НА СООБЩЕНИЕ =====
def send(bot, message, text):
    bot.send_message(
        message.chat.id,
        text,
        reply_to_message_id=message.message_id
    )


# ===== ГЛАВНАЯ ФУНКЦИЯ =====
def run(bot, message, text):
    text = text.strip().lower()


    # ===== ПРОСТО "ФУНЯ" =====
    if text == "":
        send(bot, message, random.choice(PHRASES))
        return


    # ===== "Я УРОД" И Т.П. =====
    if is_question(text):
        send(bot, message, random.choice(YES_NO))
        return


    # ===== "ДА ИЛИ НЕТ" =====
    if "да или нет" in text:
        send(bot, message, random.choice(YES_NO))
        return


    # ===== ЕСЛИ НЕ ПОНЯЛ =====
    send(bot, message, "🤖 Не понял вопрос")
