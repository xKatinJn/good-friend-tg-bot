import os
import aiohttp

from aiogram import types

from utils import log


WEB = os.environ.get("WEB_ADDRESS")


@log
async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )


@log
async def test_celery(event: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{WEB}/test_celery") as response:
            result = await response.text()
    await event.answer(
        result,
        parse_mode=types.ParseMode.HTML,
    )
