from database import update_balance
from datetime import datetime
import pytz
from config import TIMEZONE

def register_handlers(bot):
    @bot.message_handler(func=lambda m: m.text == "🎁 Бонус")
    def bonus_command(message):
        tz = pytz.timezone(TIMEZONE)
        now = datetime.now(tz)
        update_balance(message.from_user.id, 2500)
        text = "🎁 Ежедневный бонус\n\n+2500 💰\n⏳ Обновление: 00:00 (Киев)"
        bot.send_message(message.chat.id, text)
