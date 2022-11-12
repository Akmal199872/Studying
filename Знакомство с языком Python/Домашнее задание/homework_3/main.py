def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)

list = [2, 3, 5, 9, 6]

result = 0
for i in list:
    if list.index(i) % 2 != 0:
        result += i
print(result)

IntroTask(2)

list2 = [2, 3, 4, 5, 6]
list3 = []
multiply = 0
size = len(list2)
i = 0

while i < ((size / 2)):
    multiply = list2[i] * list2[size - i - 1]
    list3.append(multiply)
    i += 1

print(list3)

IntroTask(3)

list4 = [6.1, 1.2, 3.1, 5, 10.01]
list5 = []

for i in list4:
    diff = round(i - int(i), 2)
    list5.append(diff)

max = list5[0]
min = 0


for i in list5:
    if i > max:
        max = i
    else:
        min = i

diff = max - min
print(round(diff, 2))

IntroTask(4)

number = int(input("Введите любое число: "))
result = ""
while number != 0:
    result += str(number % 2)
    number //= 2
print(result)

IntroTask(5)

def PositiveFibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return PositiveFibonacci(n - 1) + PositiveFibonacci(n - 2)

def NegativeFibonacci(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        number1 = 1
        number2 = -1
        for i in range(2, n):
            number1, number2 = number2, number1 - number2
        return number2

list = []
for e in range(1, 9):
    list.append(PositiveFibonacci(e))
    list.insert(0, NegativeFibonacci(e))
print(list)