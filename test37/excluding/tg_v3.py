from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio
from run import read_messages
from random import randint

TOKEN = "8058619612:AAGFt_YQNVzSpg7xPOno8hsX_319kTGqy84"
CHAT_ID = -1002283064413


async def send_messages(update: Update, context: CallbackContext, th_id: int = 0):
    posted_ids = set()
    msgs = read_messages()
    posted_ids 
    while True:
        len_posted = len(posted_ids)
        msgs = read_messages()
        for id, msg in msgs.items():
            if id not in posted_ids:
                await context.bot.send_message(chat_id=CHAT_ID, text='\n'.join(msg), message_thread_id = th_id)
                posted_ids.add(id)
            await asyncio.sleep(0.5)
        if len_posted == len(posted_ids):
            await asyncio.sleep(60+randint(3,8))
        await asyncio.sleep(randint(3,8))

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Бот начал работу. Дальше твиты...")
    await send_messages(update, context)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()
