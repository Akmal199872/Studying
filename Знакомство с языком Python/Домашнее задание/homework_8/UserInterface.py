import ReadWriteData as rwd
import ChangeSearchData as csd
import random


def choose_action():
    while True:
        print('В рамках данной программы вам доступны следующие действия:')
        actions = ['Добавление студента', 'Посмотреть всех студентов', 'Поиск по данным студента', 'Изменение данных о студенте', 'Выйти из программы']
        nums = [i for i in range(1, 6)]
        list_actions = list(zip(nums, actions))
        print(list_actions)
        number = int(input("Введите номер действия: "))
        if number == 1:
            rwd.write_data(file_name='UniversityDatabase.txt',
                               id_num=random.randint(0000, 9999),
                               surname='Карпов',
                               name='Пётр',
                               middle_name='Степанович',
                               phone_number='+7 (900) 853-24-39',
                               position='Студент',
                               salary=2500)
        elif number == 2:
            rwd.read_data('UniversityDatabase.txt')
        elif number == 3:
            csd.search_existing_data(filename='UniversityDatabase.txt',
                                         id_num=None,
                                         surname='Карпов',
                                         name=None,
                                         middle_name=None,
                                         phone_number=None,
                                         position=None,
                                         salary=None)
        elif number == 4:
            csd.change_existing_data(filename='UniversityDatabase.txt',
                                     id_num=None,
                                     surname=None,
                                     name='Пётр',
                                     middle_name=None,
                                     phone_number=None,
                                     position=None,
                                     salary=None,
                                     replace='Вадим')
        else:
            print('Введена неверная цифра. Хотите выйти? Да/Нет')
            reply = input()
            if reply == 'Да':
                print('Программа завершается.')
                exit()
            else:
                print('Тогда введите корректное число.')

choose_action()