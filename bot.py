from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from openai import AsyncOpenAI
import asyncio
import logging

# Конфигурация
API_TOKEN = 'your_telegram_bot_token'
OPENAI_KEY = 'your_openai_api_key'
MODEL_NAME = 'gpt-4o-mini'

# Инициализация клиента OpenAI
client = AsyncOpenAI(api_key=OPENAI_KEY)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def ask_openai(prompt: str) -> str:
    """Функция для взаимодействия с OpenAI API"""
    try:
        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"OpenAI API Error: {e}")
        return "Извините, произошла ошибка при обработке запроса."

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот с интеграцией OpenAI. Задайте мне вопрос!")

@dp.message(Command("ask"))
async def ask_command(message: Message):
    user_query = message.text.replace('/ask', '').strip()
    if not user_query:
        return await message.answer("Напишите вопрос после команды /ask")
    
    await message.answer("Думаю...")
    response = await ask_openai(user_query)
    await message.answer(response, parse_mode="Markdown")

@dp.message()
async def handle_text(message: types.Message):
    try:
        # Отправляем действие "печатает" с помощью строкового параметра
        await bot.send_chat_action(
            chat_id=message.chat.id,
            action="typing" 
        )
        response = await ask_openai(message.text)
        await message.answer(response, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error: {e}")
        await message.answer("⚠️ Произошла ошибка")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())