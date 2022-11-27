import re


def reading_file(file_name_output, file_name_input):
    with open(file_name_output, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            with open(file_name_input, 'a', encoding='utf-8') as f2:
                f2.write(line)


# reading_file('ImportFromAddrBook.txt', 'AddressBook.txt')
