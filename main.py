import asyncio
import os

from aiogram import Bot, Dispatcher
from app.handlers.handlers import router
from dotenv import load_dotenv


async def main() -> None:
    load_dotenv()
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())