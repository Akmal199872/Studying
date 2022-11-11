import math


def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)

a = float(input("Введите число а: "))
b = float(input("Введите число b: "))

sum = a + b
diff = a - b
multiply = a * b
divide = a // b
div_left = a % b
math_calc = math.sqrt(((a**10) + (b**10)))

print(sum)
print(diff)
print(multiply)
print(divide)
print(int(divide))
print(div_left)
print(round(math_calc))

IntroTask(2)

RandomNumber = int(input("Введите любое число: "))
sum = 0
temp = RandomNumber
while sum < 100:
    RandomNumber = temp
    sum += RandomNumber
    print(sum)

IntroTask(3)

i = 1

while i <= RandomNumber:
    result = 3 * i + 1
    print(f'{i} => {result}')
    i += 1

IntroTask(4)

FirstSentence = string(input("Введите первое слово: "))
SecondSentence = string(input("Введите второе слово: "))

start = 0
count = 0
end = len(FirstSentence)

while FirstSentence.find(SecondSentence,start,end) != -1:
    start = FirstSentence.find(SecondSentence, start, end) + len(SecondSentence)
    count += 1
print(count)
