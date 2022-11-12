def IntroTask(number):
    print("\nЗадача №", number, "\n")


IntroTask(1)

# colors = ['red', 'green', 'blue', 'orange']
# data = open('file.txt', 'w')
#
# data.writelines(colors)
# data.write('\nLINE 12\n')
# data.write('LINE 3\n')
# data.close()

with open('file.txt', 'w') as data:
    data.write('LINE 1\n')
    data.write('LINE 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

IntroTask(2)

def new_string(symbol, count):
    return symbol * count

print(new_string('!', 3))

IntroTask(3)

def concantenation(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concantenation('a', 's', 'd', 'w'))

IntroTask(4)

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

list = []
for e in range(1,10):
    list.append(fib(e))
print(list)

IntroTask(5)

a = (3, 4, 5, 8)
print(a)
print(a[0])
print(a[-1])

for item in a:
    print(item)

dictionary = {}
dictionary = \
    {
        'Алексей': '14-37',
        'Мария': '85-78',
        'Степан': '16-76',
        'Пётр': '45-65'
    }
print(dictionary)
print(dictionary['Мария'])

for k in dictionary.keys():
    print(k)

for k in dictionary.values():
    print(k)

IntroTask(6)

colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red')
colors.add('gray')
colors.remove('red')
colors.discard('red')
colors.clear()
print(colors)

IntroTask(7)

a = {1, 2, 3, 5, 8}
b = {1, 2, 3, 4, 21}
c = a.copy()
u = a.union(b)
i = a.intersection(b)
dl = a.difference(b)
dr = b.difference(a)

print(i)

IntroTask(8)

list = [1, 2, 3, 4, 5]
list2 = list

for e in list:
    print(e)

print()

for e in list2:
    print(e)

list[0] = 123
list2[2] = 333
for e in list:
    print(e)

print()

for e in list2:
    print(e)

IntroTask(9)

list = [1, 2, 3, 4, 5]
print(len(list))
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.pop(0))
print(list)
print(list.insert(0, 11))
print(list.append(16))
print(list)

