import telegram
from app.config import setting

# Define bot
bot = telegram.Bot(token=setting.TELEGRAM_BOT_TOKEN)


async def send_message_telegram(message: str, parse_mode: str = "Markdown"):
    await bot.send_message(chat_id=setting.TELEGRAM_CHAT_ID, text=message, parse_mode=parse_mode)
