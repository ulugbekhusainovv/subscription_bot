from aiogram.filters import Command
from loader import dp
from aiogram import types


@dp.message(Command('help'))
async def help_bot(message:types.Message):
    await message.answer("Sizga qanday yordam kerak?")
