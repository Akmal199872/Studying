def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)

number = str(input("Введите любое число: "))
sum = 0

for i in number:
    if i.isdigit():
        sum += int(i)

print(sum)

IntroTask(2)

number = int(input("Введите любое число: "))
i = 1
result = 1
while i <= number:
    result *= i
    print(result)
    i += 1

IntroTask(3)

number = int(input("Введите любое число: "))
i = 1
result = 0
while i <= number:
    result += (1 + (1/i)) ** i
    i += 1
print(f'{i} => {result}')

IntroTask(4)

list = []
number = int(input("Введите любое число: "))
negativeNumber = number * -1
while (negativeNumber <= number):
    list.append(negativeNumber)
    negativeNumber += 1

index = [1, 2, 3]

result = 1
for i in index:
    result *= list[i]
print(result)
IntroTask(5)

list = [int(x) for x in input().split()]
for j, item in enumerate(list):
    if item % 2 == 0 and j > 0:
        list[j], list[j - 1] = list[j - 1], list[j]
    elif item % 2 != 0 and j < len(list) - 1:
        list[j], list[j + 1] = list[j + 1], list[j]
print(*list, sep=" ", end="")