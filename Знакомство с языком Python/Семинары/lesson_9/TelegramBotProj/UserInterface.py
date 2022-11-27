import exportContact as expC
import importContact as impC
import addContact as addC
import removeContact as rmC
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def choose_action():
    while True:
        print('В рамках данной программы вам доступны следующие действия:')
        actions = ['Добавление контакта', 'Удаление контакта', 'Импорт контактов', 'Экспорт контактов']
        nums = [i for i in range(1, 5)]
        list_actions = list(zip(nums, actions))
        print(list_actions)
        number = int(input("Введите номер действия: "))
        if number == 1:
            addC.add_new_contact('Карпов', 'Вадим', 'Степанович', '+7 (915) 361-39-60')
        elif number == 2:
            rmC.remove_existing_contact(None, 'Константин', None, None)
        elif number == 3:
            expC.reading_file('ImportFromAddrBook.txt', 'AddressBook.csv')
        elif number == 4:
            impC.reading_file('ImportFromAddrBook.txt', 'AddressBook.txt')
        else:
            print('Введена неверная цифра. Попробуйте ещё раз')