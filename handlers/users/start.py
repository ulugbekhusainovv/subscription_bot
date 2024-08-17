from aiogram.filters import CommandStart
from loader import dp
from aiogram import types
import sqlite3


conn = sqlite3.connect('bot.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(30) NULL,
        full_name TEXT,
        telegram_id INTEGER,
        lang_code VARCHAR(10) NULL,
        registration_date TEXT
    )
''')
conn.commit()

@dp.message(CommandStart())
async def start_bot(message:types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}! user")
