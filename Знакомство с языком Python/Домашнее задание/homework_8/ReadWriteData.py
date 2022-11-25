import EmployeeParams as emp_par
import random


def write_data(file_name, id_num, surname, name, middle_name, phone_number, position, salary):
    with open(file_name, 'a', encoding='utf-8') as f:
        print(f.write(emp_par.add_new_data(id_num=id_num, surname=surname, name=name, middle_name=middle_name, phone_number=phone_number, position=position, salary=salary)))


# write_data(file_name='UniversityDatabase.txt', id_num=random.randint(0000, 9999), surname='Карпов', name='Пётр', middle_name='Степанович', phone_number='+7 (900) 853-24-39', position='Студент', salary=2500)


def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        print(f.read())


# read_data('UniversityDatabase.txt')