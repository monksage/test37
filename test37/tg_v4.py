from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Application
import asyncio
import time
from random import randint
from run import read_messages
# from json_parser import test_extract as read_messages
from env_extract import ENV, get_env
from datetime import datetime
import pytz


def replacer_md2(string: str):
    return string

# Функция для отправки сообщений
async def send_message(update: Update, context: CallbackContext, message: str, chat_id: int, theme_id: int):
    await context.bot.send_message(chat_id=chat_id, text='\n'.join(message[1:]), message_thread_id = theme_id, parse_mode='Markdown')
    await asyncio.sleep(1)  # Пауза в полсекунды

# Основная функция бота
async def bot(update: Update, context: CallbackContext, chat_id: int, theme_id: int):
    # posted_ids = set()
    messages = read_messages()
    posted_ids = set(messages.keys())
    await send_message(update, context, ['Бот включился в:', f'{datetime.now(pytz.timezone("Europe/Moscow"))} по Московскому времени'], chat_id, theme_id)
    await asyncio.sleep(10)
    while True:
        # Чтение сообщений
        messages = read_messages()
        
        # Обработка каждого сообщения
        for id, message in messages.items():
            if id not in posted_ids:
                # Отправка сообщения
                try:
                    # print(message)
                    await send_message(update, context, message, chat_id, theme_id)
                except:
                    if len(posted_ids) > 500:
                        posted_ids = set(sorted(list(posted_ids))[100::-1])
                    await asyncio.sleep(60)
                # Сохранение ID отправленного сообщения
                posted_ids.add(id)
        
        # Пауза между запросами read_messages
        await asyncio.sleep(randint(3,7))  # Пауза в 1 секунду

# Команда для запуска бота
async def start(update: Update, context: CallbackContext):
    env = get_env()
    chat_id = env.CHAT_ID
    theme_id = env.THEME_ID
    bot_ = await bot(update, context, chat_id, theme_id)
    await asyncio.run(bot_)


# Основная функция для запуска бота
def main():
    env:ENV = get_env()
    application = Application.builder().token(env.TOKEN).build()
    application.add_handler(CommandHandler(env.COMMAND_START, start))
    application.run_polling()
    

# Запуск бота
if __name__ == "__main__":
    main()
