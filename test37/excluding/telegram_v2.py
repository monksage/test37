from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio
from run import read_messages, return_unread, randint

# Замените на ваш токен
TOKEN = "8058619612:AAGFt_YQNVzSpg7xPOno8hsX_319kTGqy84"
CHAT_ID = -1002258653205
CHAT_ID = -1002283064413
latest_msgs = []

async def send_messages(update: Update, context: CallbackContext):
    global latest_msgs
    chat_id = CHAT_ID
    await context.bot.send_message(chat_id = chat_id, text = 'https://x.com/HieroTerminal/status/1888177305748398400', message_thread_id = 2)
    await context.bot.send_message(chat_id = chat_id, text = '"Wow\n\n- ~~                    ~~\n> **Bernie** (**[@Artemisfornow](https://x.com/Artemisfornow)**)\n> 🤡 GLOBALIST MELTDOWN -  Gordon in a panic about USAID being shut down.\n> \n> So let me be clear… Gordon is now the:\n> \n> ▪️United Nations Special Envoy for Global Education,\n> \n> AND \n> \n> ▪️World Health Organization’s (WHO) Ambassador for Global Health Financing\n> \n> AND\n> \n> ‼️USAID allocated approximately [$21](https://x.com/search?q=%2421).4 BILLION to programs implemented through the United Nations and other international organisations, which include the WHO‼️\n> \n> We see you Gordon, we see you 🤡 **[View More](https://x.com/Artemisfornow/status/1887930755353035103)**\n> - :frame_photo: — **[Image #1](https://pbs.twimg.com/media/GjNHA2MXIAEzZyG.jpg)**\n- ~~                    ~~",', message_thread_id = 2)
    # while True:h
    #     sleep_time = randint(3,7)
    #     msgs = read_messages()
    #     latest_msgs, new_msgs = return_unread(msgs=msgs, latest_msgs=latest_msgs)
        
    #     # print(new_msgs)
    #     # print(latest_msgs)
    #     try: 
    #         if new_msgs:
    #             for message in new_msgs:
    #                 await context.bot.send_message(chat_id=chat_id, text=message)
    #         else:
    #             await asyncio.sleep(60+sleep_time)
    #         await asyncio.sleep(sleep_time)  # Ожидание 5 секунд перед следующей проверкой
    #     except:
    #         latest_msgs = latest_msgs
    #         print('exception catched!')
    #         await asyncio.sleep(sleep_time)

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Бот начал работу. Дальше твиты...")
    await send_messages(update, context)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
