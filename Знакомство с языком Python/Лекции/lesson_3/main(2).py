def IntroTask(number):
    print("\nЗадача №", number, "\n")


IntroTask(1)


# path = 'file.txt'
# file = open(path, 'r')
# data = file.read() + ' '
# file.close()


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)
print(res)


li = [x for x in range(1,21)]
li = list(map(lambda x: x + 10, li))
print(li)

# data = list(map(int, input().split()))
# print(data)
#
# print(data)



data = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data))

print(res)


users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)
data2 = list(enumerate(users))
print(data2)