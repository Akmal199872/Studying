import re


def search_existing_data(filename, id_num, surname, name, middle_name, phone_number, position, salary):
    func_args = locals()
    for i, j in func_args.items():
        if j is not None:
            pattern = re.compile(re.escape(j))
            with open(filename, 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    result = pattern.search(line)
                    if result is not None:
                        print(line)


# search_existing_data(filename='UniversityDatabase.txt', id_num=None, surname='Карпов', name=None, middle_name=None, phone_number=None, position=None, salary=None)


def change_existing_data(filename, id_num, surname, name, middle_name, phone_number, position, salary, replace):
    func_args = locals()
    for i, j in func_args.items():
        if j is not None:
            pattern = re.compile(re.escape(j))
            with open(filename, 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        print(line)
                        data = line.replace(j, replace)
                        f.write(data)


# change_existing_data(filename='UniversityDatabase.txt', id_num=None, surname=None, name='Пётр', middle_name=None, phone_number=None, position=None, salary=None, replace='Вадим')