import math
import random


def IntroTask(number):
    print(f"\nЗадача №{number}\n")


IntroTask(1)

stringNumber = input("Введите вещественное число: ")
count = 0

if float(stringNumber) < 0:
    stringNumber = str(float(stringNumber) * (-1))

for i in range(len(stringNumber)):
    if stringNumber[i] == '.':
        continue
    else:
        count += int(stringNumber[i])
print(count)

IntroTask(2)

number1 = int(input("Введите любое число: "))
mass = [math.factorial(i) for i in range(1, number1 + 1)]
print(mass)

IntroTask(3)

mass = [round(((1+1/i) ** i), 2) for i in range(1, number1 + 1)]
print(mass)

IntroTask(4)

mass = [round((2 * i + 1), 2) for i in range(-number1, number1 + 1)]
print(mass)

IntroTask(5)

listArray = list(map(int, input(f"Введите {number1} значений массива через пробел: ").split()))
result = 1
for i in listArray:
    result *= mass[i]
print(result)

IntroTask(6)

listArray = [i for i in range(random.randint(3, 6))]
print(listArray)
random.shuffle(listArray)
print(listArray)

IntroTask(7)

for i in range(len(listArray) - 1):
    listArray[i], listArray[i + 1] = listArray[i + 1], listArray[i]
print(listArray)

IntroTask(8)

listArray = list(map(int, input("Введите значения массива через пробел: ").split()))
listArray2 = []
count = 0
for i in listArray:
    if i in listArray2:
        continue
    else:
        listArray2.append(i)
        count += 1
print(f'Количество уникальных значений в списке = {count} из {len(listArray)}')
print(listArray2)

IntroTask(9)

listArray = ['привет', 'да', 'может быть', 'не может быть', 4, 'так', 'ладно', 'неплохо', 7, 'отлично', 9]
print(listArray)
for i in listArray:
    if type(i) == int:
        print(i, end=" ")

IntroTask(10)
searchText = input("Введите искомую строку: ")
listArray2 = [i for i in range(1, len(listArray)) if listArray[i] == searchText]
print(listArray2)