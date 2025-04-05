import httpx
import asyncio
import json
import os
from datetime import datetime
from telegram import Bot
from telegram.ext import CommandHandler, Application
from dotenv import load_dotenv
import numpy as np

# Загружаем переменные окружения
load_dotenv(override=True)

# Константы API CoinGecko и Telegram
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Инициализируем Telegram Bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Функция для отправки сообщений в Telegram
def send_telegram_message(message):
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")


# Функция для получения данных о криптовалюте
async def get_crypto_data(crypto_id="bitcoin"):
    url = f"{COINGECKO_BASE_URL}/coins/{crypto_id}/market_chart"
    params = {"vs_currency": "usd", "days": "30"}  # За последние 30 дней
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data["prices"]  # Возвращаем цены
        except Exception as e:
            print(f"Ошибка получения данных: {e}")
            return []


# Функция для вычисления Moving Average (MA)
def calculate_moving_average(prices, window=14):
    # Создаем DataFrame для упрощения работы с данными
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df['ma'] = df['price'].rolling(window=window).mean()
    return df['ma'].iloc[-1]  # Возвращаем последнее значение MA


# Функция для вычисления RSI (Relative Strength Index)
def calculate_rsi(prices, window=14):
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    delta = df['price'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]  # Возвращаем последнее значение RSI


# Функция для генерации торговых сигналов
async def generate_trade_signals(crypto_id="bitcoin"):
    prices = await get_crypto_data(crypto_id)
    if not prices:
        return "Не удалось получить данные для анализа."

    # Вычисляем индикаторы
    moving_average = calculate_moving_average(prices)
    rsi = calculate_rsi(prices)

    signals = []

    # Пример простых торговых сигналов:
    if rsi > 70:
        signals.append(f"⚠️ RSI ({rsi:.2f}) указывает на перепроданность. Рассмотрите возможность продажи!")
    elif rsi < 30:
        signals.append(f"⚠️ RSI ({rsi:.2f}) указывает на перепокупку. Рассмотрите возможность покупки!")
    else:
        signals.append(f"RSI ({rsi:.2f}) в нормальном диапазоне. Ожидайте дальнейших сигналов.")

    if prices[-1][1] > moving_average:
        signals.append(f"📈 Цена выше MA ({moving_average:.2f}), что может указывать на покупку.")
    else:
        signals.append(f"📉 Цена ниже MA ({moving_average:.2f}), что может указывать на продажу.")

    return "\n".join(signals)


# Обработчик команды /start
async def start(update, context):
    await update.message.reply_text("Привет! Я бот для анализа криптовалютных сигналов. Отправь команду /signals для получения текущих сигналов.")


# Обработчик команды /signals
async def signals(update, context):
    signals = await generate_trade_signals()
    await update.message.reply_text(signals)


# Функция для отправки реферальных ссылок
async def referral(update, context):
    referral_link = "https://www.cryptobirja.com/referral"  # Замените на вашу реферальную ссылку
    await update.message.reply_text(f"Зарегистрируйтесь на криптобирже по моей ссылке и получите бонус: {referral_link}")


# Основной цикл работы бота
async def main():
    # Инициализируем приложение
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signals", signals))
    application.add_handler(CommandHandler("referral", referral))

    # Запускаем бота
    print("Бот запущен. Ожидаю команд...")
    await application.run_polling()


# Запуск основного процесса
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
