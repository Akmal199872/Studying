import random
import numpy as np
def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)

b = [int(i) for i in input().split()]

k = int(input("Введите максимальное количество элементов в массиве: "))
a = []
# for _ in range(k):
#     a.append(int(input()))

i = 0
# while i < k:
#     a.append(int(input()))
#     i += 1

while True:
    s = input()
    if s != "":
        a.append(int(s))
    else:
        break

IntroTask(2)

a = [int(i) for i in input().split()]
p_1 = 0
p_2 = len(a) - 1

while p_1 <= p_2:
    print(a[p_1] * a[p_2])
    p_1 += 1
    p_2 -= 1

IntroTask(3)

c = [int(i) for i in input().split()]
min = c[0] - int(c[0])
max = c[0] - int(c[0])

for num in c:
    if num - int(num) > max:
        max = num - int(num)
    elif num - int(num) < min:
        min = num - int(num)

print(max - min)

IntroTask(4)

size = int(input())
array = []
i = 0

while i < size:
    number = random.randint(1, 9)
    array.append(number)
    i += 1

print(array)

min = 0
max = array[0]


for j in array:
    if j > max:
        max = j
    else:
        min = j


print(f"{min} {max}")

IntroTask(5)

a,b,c = int(input()), int(input()), int(input())
print(np.roots(a,b,c))

