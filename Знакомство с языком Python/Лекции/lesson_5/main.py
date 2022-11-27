from isOdd import isOdd
from progress.bar import Bar
import time
import emoji
import matplotlib.pyplot as plt
import numpy as np
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def IntroTask(number):
    print(f"\nЗадача №{number}\n")


IntroTask(1)

print(isOdd(1))
print(isOdd(5))

print(isOdd(0))
print(isOdd(4))

IntroTask(2)

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(0)
    bar.next()
bar.finish()

IntroTask(3)

print(emoji.emojize('python is :thumbs_up:'))

IntroTask(4)

np.random.seed(19680801)
plt.rcdefaults()
fig, ax = plt.subplots()

plt.show()

IntroTask(5)

list = [random.randint(1, 9) for i in range(1, 6)]
plt.plot(list)

plt.show()

IntroTask(6)


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('mytoken')
updater.dispatcher.add_handler(CommandHandler('hello', hello))
print('server start')
updater.start_polling()
updater.idle()
