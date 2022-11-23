def log_expression(a):
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write(f'Уравнение: {a} = 0\n')


def log_ans(a):
    with open('file.txt', 'a', encoding='utf-8') as f:
        f.write(f'Ответ: {a}\n')
