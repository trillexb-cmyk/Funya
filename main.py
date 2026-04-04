@bot.message_handler(func=lambda message: True)
def handler(message):
    if not message.text:
        return

    text = message.text
    text_low = text.lower()

    # ===== КНОПКИ =====
    if text in [
        "👤 Профиль", "🎁 Бонус",
        "⚒ Кузня", "🛒 Магазин", "👥 Команды",
        "🏆 Турниры",
        "💬 Чаты", "👥 Кланы",
        "🎮 Игры",
        "📜 Политика", "📞 Связь"
    ]:
        menu.handle_buttons(bot, message)
        return

    # ===== РЕАКЦИЯ НА ФУНЯ =====
    if text_low.startswith("фуня"):
        
        if "меню" in text_low:
            menu.send_menu(bot, message.chat.id)

        elif "профиль" in text_low:
            profile.show_profile(bot, message)

        elif "баланс" in text_low:
            economy.show_balance(bot, message)

        elif "бонус" in text_low:
            economy.get_bonus(bot, message)

        elif "перевод" in text_low:
            economy.transfer(bot, message)

        else:
            bot.send_message(
                message.chat.id,
                "🤖 Напиши: помощь, профиль, бонус"
            )

        return

    # ===== ВСЁ ОСТАЛЬНОЕ — ИГНОР =====
    return
