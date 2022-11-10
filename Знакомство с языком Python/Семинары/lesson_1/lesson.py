def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)
# Задача №1

a = -9
b = 3
print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a ** b)
print(a // b)
print(a % b)

# Задача №2

IntroTask(2)

if a % 3 == 0:
    print("Делится")
else:
    print("Не делится")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if (a ** 2 == b or b ** 2 == a):
    print("Число является квадратом")
else:
    print("Число не является квадратом")

# Задача №3

IntroTask(3)

list = [int(i) for i in input("Введите число: ").split()]

max = list[0]
print(list)

for i in list:
    if i > max:
        max = i

print(max)

# Задача №4

IntroTask(4)

for i in range(-a, a + 1):
    print(i, end = ' ')

# Задача №5

IntroTask(5)

a = float(input("Введите число: "))
b = a % 1
c = b * 10

print(int(c))
