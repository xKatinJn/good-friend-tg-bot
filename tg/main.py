import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from polls import start_handler


load_dotenv(".env")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=TG_BOT_TOKEN)
dispatcher = Dispatcher(bot=bot)


async def main():
    global bot, dispatcher
    try:
        dispatcher.register_message_handler(
            start_handler, commands={"start", "restart"}
        )
        await dispatcher.start_polling()
    finally:
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
