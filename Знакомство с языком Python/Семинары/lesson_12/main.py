list1 = [1, 34, 2, 56, 7, 3]
list2 = [35, 78, 56]
list3 = [23, 34, 567, 67, 34, 23, 64]

a, b, c = list2
print(f'a = {a}, b= {b}, c= {c}')

a, b, *c = list1
print(f'a = {a}, b = {b}, c = {c}')

a, *b, c = list3
print(f'a = {a}, b = {b}, c = {c}')

list4 = [(23, 34), (567, 67), (34, 23)]

for i, j in list4:
    print(f'i = {i}, j = {j}')

# Словарь:
my_dict = dict(list4)
print(f'\nСловарь:\n{my_dict}')