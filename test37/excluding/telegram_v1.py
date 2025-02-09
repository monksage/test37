from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Конфигурация
BOT_TOKEN = "8058619612:AAGFt_YQNVzSpg7xPOno8hsX_319kTGqy84"  # Замените на токен вашего бота
TARGET_CHAT_ID = -1002258653205  # Замените на ID чата, куда пересылать сообщения

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Пересылает сообщение в указанный чат."""
    try:
        # Пересылаем сообщение
        await context.bot.send_message(
            chat_id=TARGET_CHAT_ID,
            text=f"Сообщение от {update.message.from_user.first_name}:\n{update.message.text}"
        )
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    # Инициализация бота
    app = Application.builder().token(BOT_TOKEN).build()

    # Обработчик текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()
