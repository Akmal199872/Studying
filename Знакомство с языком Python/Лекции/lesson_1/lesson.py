print("Hello World")

a = 233
b = 2.3333
print(a)
print(type(b))

value = 12334
print(type(value))

s = 'qwerty'
print(s)

# 
# 
# 

print(a,' - ', b, ' - ', s)
print('{} - {} - {}'.format(a,b,s))
print(f'{a} - {b} - {s}')
print('{1} - {2} - {0}'.format(a,b,s))


f = True
print(type(f))

list = [1,2,3]
print(list)


# print("Введите а")
# a = int(input())
# print("Введите b")
# b = int(input())
print(a, ' + ', b, ' = ', a + b)
print(a, ' + ', b, ' = ', a / b)
print(a, ' + ', b, ' = ', a ** b)


a = 1.3
b = 3
c = round(a*b, 3)

f = [1,2,3,4]
print(f)
print(2 in f)

is_odd = f[0] % 2 == 0
print(is_odd)

is_odd = not f[0] % 2
print(is_odd)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(original)
else:
    print("Пожалуй")
    print("Хватит!")

print(inverted)

list = [1,2,3,4,5]
for i in list:
    print(i**2)


for i in range(1, 10, 2):
    print(i)

for i in 'qwe - rty':
    print(i)

text = 'съешь ещё этих мягких булок'

print(text[0])
print(text[1])
# print(text(len(text)))
print(text[len(text) - 1])
print(text[-5])
print(text[:])
print(text[:])
print(text[len(text) - 2:])
print(text[2:9])
print(text[6:-18])
print(text[0:len(text):6])
print(text[::6])

def f(x):
    if x == 1:
        return "Целое"
    elif x == 2.3:
        return 23

print(f(1))

