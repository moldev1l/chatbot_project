import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import CommandStart
import config
# Вставь свой токен бота

TOKEN = config.token

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я эхо-бот. Напиши мне что-нибудь!")

# Эхо-ответ на все сообщения
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Ты написал: {message.text}")

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
