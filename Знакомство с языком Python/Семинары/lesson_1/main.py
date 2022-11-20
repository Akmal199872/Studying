def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)

def powNumber(number):
    return number**2

print(powNumber(4))

IntroTask(2)

# number1, number2 = int(input("Введите первое число: ")), int(input("Введите второе число: "))

arrayNumber = input("Введите любое число: ").split()
number1 = int(arrayNumber[0])
number2 = int(arrayNumber[1])

if number1 ** 2 == number2:
    print("Второе число является квадратом первого")
elif number2 ** 2 == number1:
    print("Первое число является квадратом второго")
else:
    print("Числа не являются квадратом друг друга")

IntroTask(3)

arrayNumber = list(map(int, input("Введите 5 разных чисел: ").split()))
print(max(arrayNumber))

IntroTask(4)

number1 = int(input("Введите любое число: "))
for i in range((number1 * -1), number1 + 1):
    print(i, end=" ")

IntroTask(5)

number1 = float(input("Введите десятичное число: "))
print(int(number1 * 10) % 10)

IntroTask(6)

number1 = int(input("Введите любое число: "))

if number1 % 5 == 0 and number1 % 10 == 0 or number1 % 15 == 0 and number1 % 30 != 0:
    print("Число кратно")
else:
    print("Число некратно")