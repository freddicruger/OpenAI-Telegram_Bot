# Telegram Bot with OpenAI Integration 🤖

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Aiogram Version](https://img.shields.io/badge/aiogram-3.x-blue)](https://docs.aiogram.dev/)
[![OpenAI API](https://img.shields.io/badge/OpenAI-1.x-green)](https://platform.openai.com/)

Умный телеграм-бот с интеграцией ChatGPT API. Отвечает на вопросы, поддерживает диалог и помогает с различными задачами.

## ✨ Особенности
- Интеграция с OpenAI GPT-3.5/4
- Асинхронная архитектура
- Поддержка команд:
  - `/start` - Приветствие
  - `/ask` - Задать вопрос
- Индикатор набора сообщения
- Обработка ошибок API

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.10+
- Аккаунт OpenAI с API ключом
- Телеграм-бот от [@BotFather](https://t.me/BotFather)

### Установка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/telegram-openai-bot.git
cd telegram-openai-bot
```

2. Установите зависимости:
```bash

pip install -r requirements.txt
```

3. Настройте окружение:
```bash

cp .env.example .env
```
Заполните параметы в bot. py:
```bash
BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```

### Запуск
```bash
python bot.py
```

## ⚙️ Конфигурация
Доступные переменные окружения:
| Переменная        | Описание                               |
|-------------------|----------------------------------------|
| `BOT_TOKEN`       | Токен телеграм-бота                    |
| `OPENAI_API_KEY`  | Ключ OpenAI API                        |
| `MODEL_NAME`      | Модель GPT (по умолчанию: gpt-4o-mini) |

## 🌍 Примеры использования
```
Пользователь: /ask Как работает ИИ?
Бот: 🤔 Думаю...
Бот: Искусственный интеллект работает путем...
```

```
Пользователь: Напиши стихотворение про космос
Бот: 🚀 В бескрайних просторах вселенской глубин...
```

[Документация Aiogram](https://docs.aiogram.dev/) | [OpenAI API Docs](https://platform.openai.com/docs)
