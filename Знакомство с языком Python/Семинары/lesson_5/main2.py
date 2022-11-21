import codecs
import math
import random
import sympy
from sympy import isprime, simplify

def IntroTask(number):
    print(f"\nЗадача №{number}\n")


IntroTask(1)


def dev_for_primes(a):
    primelist = []
    for i in range(1, a):
        if isprime(i) and a % i == 0:
            while a % i == 0:
                primelist.append(i)
                a //= i
    return primelist


print(dev_for_primes(144))

IntroTask(2)


def gen_pol(n):
    polinom = ''
    for i in range(n + 1):
        if i == 0:
            polinom += str(random.randint(1, n)) + '*x**' + str(n - i)
        elif i == n:
            polinom += '+' + str(random.randint(1, n))
        else:
            polinom += '+' + str(random.randint(1, n)) + '*x**' + str(n - i)
    polinom += '=0'
    return polinom


with open('file.txt', 'w') as f:
    f.write(gen_pol(2))
    f.close()
print((open('file.txt', 'r').read()))

IntroTask(3)

with open('file.txt', 'r') as f:
    readData = f.read()

coupleStr = sympy.simplify('readData')

with open('file2.txt', 'w') as f:
    writeData = f.write(str(coupleStr))

IntroTask(4)

listArray = list(map(int, input("Введите числа через пробел: ").split()))
print(listArray)
tempArray = []

for i in range(1, len(listArray) + 1):
    if i in listArray:
        continue
    else:
        tempArray.append(i)
print(tempArray)

IntroTask(5)

file = open('file2.txt', 'w')
data = file.write('Баржа, вода, битва, Беверли, воображуля, вброс, виноград, Парсер')
file.close()

file = open('file2.txt', 'r')
data = file.read() + ' '
file.close()
print(data)

words = list(filter(lambda x: not x.casefold() == 'а' and not x.casefold() == 'б' and not x.casefold() == 'в', data))
reply = ''.join(words)
print(reply)

IntroTask(6)

listArray = [random.randint(1, 9) for i in range(random.randint(3, 9))]
tempArray = []
print(listArray)

for i in range(len(listArray)):
    if listArray[i] == max(listArray[:i + 1:]) and listArray[i] not in tempArray:
        tempArray.append(listArray[i])
print(tempArray)