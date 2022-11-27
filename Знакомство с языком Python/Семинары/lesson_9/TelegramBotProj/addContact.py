def add_new_contact(surname, name, middle_name, phone_number):
    data = f'{surname} {name} {middle_name}, тел.: {phone_number}\n'
    with open('AddressBook.txt', 'a', encoding='utf-8') as f:
        f.write(data)


# add_new_contact('Карпов', 'Вадим', 'Степанович', '+7 (915) 361-39-60')
