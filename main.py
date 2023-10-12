from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

import asyncio
from loguru import logger
from settings import Config, load_config
from handlers import router_list
from settings import ConnectDb


async def main():

    logger.info("bot is loading")
    config: Config = load_config()
    ConnectDb.connection
    logger.info("connect to BD")
    from aiogram.fsm.storage.memory import MemoryStorage
    storage = MemoryStorage()
    bot = Bot(config.bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=storage)

    logger.info("connect routers")

    dp.include_router(*router_list)

    logger.info("bot is starting")
    try:
        await dp.start_polling(bot)
        logger.info("disconnect")
    finally:
        await dp.storage.close()
        await bot.session.close()
        logger.info("Bot is off")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")
