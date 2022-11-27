from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import RationNum as num_object
# import ComplexNum as num_object
import datetime
import math as m
import cmath as cm
import UserInterface as ui


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def user_interface_for_addr_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{ui.choose_action()}')

async def calculating_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    list_activities = dir(m)
    result = 0
    for i, j in enumerate(list_activities, start=1):
        await update.message.reply_text(f'№{i} = Функция: "{j}"')
    function_number = int(input("Выберите необходимую функцию: "))
    await update.message.reply_text(f'{num_object.choose_func(function_number)}')

    # ui.choose_action()

app = ApplicationBuilder().token("5978023098:AAFyfMqr5ITSQ2b").build()
print('server start')
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("calculating", calculating_numbers))
app.add_handler(CommandHandler("addressbook", user_interface_for_addr_book))

app.run_polling()

