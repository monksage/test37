import asyncio
import time

# Предположим, что у вас есть функция read_messages, которая возвращает список сообщений
async def read_messages():
    # Здесь должен быть код для чтения сообщений
    # Например, возвращаем тестовые данные
    return [
        {"id": 1, "text": "Сообщение 1"},
        {"id": 2, "text": "Сообщение 2"},
        {"id": 3, "text": "Сообщение 3"},
    ]

# Функция для отправки сообщений
async def send_message(message):
    # Здесь должен быть код для отправки сообщения
    print(f"Отправлено сообщение: {message['text']}")
    await asyncio.sleep(0.5)  # Пауза в полсекунды

# Список для хранения отправленных сообщений
posted_ids = set()

async def bot():
    while True:
        # Чтение сообщений
        messages = await read_messages()
        
        # Обработка каждого сообщения
        for message in messages:
            if message['id'] not in posted_ids:
                # Отправка сообщения
                await send_message(message)
                
                # Сохранение ID отправленного сообщения
                posted_ids.add(message['id'])
        
        # Пауза между запросами read_messages
        await asyncio.sleep(1)  # Пауза в 1 секунду

# Запуск бота
async def main():
    await bot()

# Запуск асинхронного цикла
if __name__ == "__main__":
    asyncio.run(main())
