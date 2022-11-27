import re


def remove_existing_contact(name, surname, middle_name, phone_number):
    func_args = locals()
    # not_none_args = list(map(lambda x: x is not None, func_args))
    # print(', '.join(i for i, j in func_args.items() if j is not None))
    for i, j in func_args.items():
        if j is not None:
            pattern = re.compile(re.escape(j))
            with open('AddressBook.txt', 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)
                    elif result is not None:
                        print(f'Удалён контакт: {line}')
                    f.truncate()


# remove_existing_contact(None, 'Константин', None, None)