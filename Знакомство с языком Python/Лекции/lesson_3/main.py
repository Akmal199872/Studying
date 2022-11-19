def IntroTask(number):
    print("\nЗадача №", number, "\n")


IntroTask(1)


def f(x):
    x**2


g = f
print(type(f))
print(f(1))
print(g(1))


def g(x):
    return x**2


print(g(4))


def calc(x):
    return x + 10


print(calc(10))


def calc2(x):
    return x * 10


print(calc2(10))


def math(op, x):
    print(op(x))


math(calc2, 10)
math(calc, 10)


# def sum(x,y):
#     return x + y


sum = lambda x, y: x + y


def multiply(x,y):
    return x * y


def calculation(op, a, b):
    print(op(a,b))
    return op(a,b)


calculation(sum, 4, 5)
calculation(multiply, 4, 5)

calculation(lambda x, y: x + y, 4, 5)


list = []

for i in range(1, 21):
    if (i % 2 == 0):
        list.append(i)
print(list)

list2 = [i for i in range(1, 21) if i % 2 == 0]
print(list2)


def f(x):
    return x ** 3

list3 = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(list3)
list4 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list4)


def pow(x):
    return x**2
list5 = [1, 2, 3, 5, 8, 15, 23, 38]
list6 = [(i, pow(i)) for i in list5 if i % 2 == 0]
print(list6)
