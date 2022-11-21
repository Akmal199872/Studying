import math
import random
import sympy


def IntroTask(number):
    print(f"\nЗадача №{number}\n")


IntroTask(1)

# listArray = list(map(int, input().split()))
# print(listArray)

listArray = [random.randint(1, 10) for i in range(random.randint(1, 10))]
print(listArray)
resultArray = [i + i for i in listArray if not i % 2 == 0]
print(resultArray)

IntroTask(2)

tempArray = []
if len(listArray) % 2 == 0:
    resultArray = [tempArray.append(listArray[i] * listArray[len(listArray) - i - 1]) for i in
                   range(len(listArray) // 2)]
else:
    resultArray = [tempArray.append(listArray[i] * listArray[len(listArray) - i - 1]) for i in
                   range(len(listArray) // 2 + 1)]
print(tempArray)

IntroTask(3)

tempArray = []
listArray = [round(random.uniform(1.0, 9.99), 1) for i in range(random.randint(1, 9))]
print(listArray)

max = listArray[0]
min = listArray[0]

for i in listArray:
    if max < i:
        max = i
for i in listArray:
    if min > i:
        min = i

print(max)
print(min)
print(max - min)

IntroTask(4)

stringText = 'as;dkaskdlkasd;'
print(stringText[0::2])
print(stringText[::-1])
print(stringText[1::3])
print(stringText[1+1::])


cutNumber = str(listArray[0])
fif = cutNumber.find('.')
print(int(cutNumber[fif + 1::]))

IntroTask(5)

number1 = random.randint(1, 9)
print(f'{number1} => {str(bin(number1))[2::]}')

IntroTask(6)

listArray = [random.uniform(1.0, 9.0) for i in range(3)]
print(listArray)
discr = (listArray[1] ** 2) - 4 * listArray[0] * listArray[2]
print(f'Дискриминант = {discr}')

if discr > 0:
    x1 = (-listArray[1] + math.sqrt(discr)) / (2 * listArray[0])
    x2 = (-listArray[1] - math.sqrt(discr)) / (2 * listArray[0])
    print(f'x1 = {x1}, x2 = {x2}')
elif discr == 0:
    x = (-listArray[1]) / (2 * listArray[0])
    print(f'x = {x}')
else:
    print("Корней нет")

