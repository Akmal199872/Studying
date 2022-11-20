def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)

number1 = int(input("Введите любое число: "))
result = -3
for i in range(0, number1):
    print(result**i)

IntroTask(2)

number1 = int(input("Введите любое число: "))
result = 0
for i in range(1, number1 + 1):
    result = 3 * i + 1
    print(f'{i}: {result}')

IntroTask(3)

stringText1 = 'Строка21111'
stringText2 = 'Строка1'
count = 0
for i in stringText1:
    for j in stringText2:
        if i == j:
            count += 1
print(count)