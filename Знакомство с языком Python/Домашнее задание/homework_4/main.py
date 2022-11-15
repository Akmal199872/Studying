import random
from math import pi
from random import randint
import numpy as np

def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)

number = int(input())
print(f"{number} => {round(pi, number)}")

IntroTask(2)

number = int(input())
issuccess = True
list = []
temp = number

while issuccess == True:
    for i in range(2, number + 1):
        if number % i == 0:
            list.append(i)
            number = int(number / i)
            issuccess = False
print(f'{temp} => {list}')

IntroTask(3)

list2 = [int(i) for i in input().split()]
list3 = []

for i in list2:
    if i not in list3:
        list3.append(i)

print(list2)
print(list3)

IntroTask(4)


def write_file(string_text):
    with open('file.txt', 'w') as data:
        data.write(string_text)


def create_mn(k):
    lst = [random.randint(0, 100) for i in range(k + 1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input())
rate = create_mn(k)
print(write_file(create_str(rate)))


IntroTask(5)

def write_file(name, string_text):
    with open(name, 'w') as data:
        data.write(string_text)

def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  # степень
    ii = l - 1  # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


k1 = int(input())
k2 = int(input())
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file1.txt", create_str(koef1))
write_file("file2.txt", create_str(koef2))

# нахождение суммы многочлена

with open('file1.txt', 'r') as data:
    st1 = data.readlines()
with open('file2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file("file3.txt", create_str(lst_new))
with open('file3.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")