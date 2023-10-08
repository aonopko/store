from aiogram import Router
from aiogram import types
from aiogram.filters import CommandObject, Command
from aiogram import Dispatcher as dp

admin_router = Router()

@admin_router.message(Command("test"))
async def any_message(message: types.Message):
    await message.answer("Hello world")
