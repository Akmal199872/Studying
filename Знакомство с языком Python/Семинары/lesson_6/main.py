import codecs
import random


def IntroTask(number):
    print(f"\nЗадача №{number}\n")


IntroTask(1)

with codecs.open('file.txt', 'r', 'utf-8') as f:
    data = f.read()

text = data.split()
for i in range(len(text)):
    if 'абв' in text[i]:
        if not text[i].isidentifier() or '_':
            text[i] = text[i][-1]
        else:
            text[i] = ''
text = ' '.join(text)

print(text)


IntroTask(2)

seq = list(input())
tempArray = []

def calculator(seq):
    while '/' in seq or '*' in seq:
        if i != -1:
            res = seq[i - 1] * seq[i + 1]
            seq.pop(i - 1)
            seq[i] = res
            seq.pop(i + 1)
        else:
            i = seq.find('/')
            if i != -1:
                res = seq[i - 1] / seq[i + 1]
                seq.pop(i - 1)
                seq[i].pop(i + 1)
            else:
                break
    while '-' in seq or '+' in seq:
        i = seq.find('-')
        if i != -1:
            res = seq[i - 1] - seq[i + 1]
            seq.pop(i - 1)
            seq[i] = res
            seq.pop(i + 1)
        else:
            i = seq.find('+')
            if i != -1:
                res = seq[i - 1] + seq[i + 1]
                seq.pop(i - 1)
                seq[i] = res
                seq.pop(i + 1)
            else:
                break



