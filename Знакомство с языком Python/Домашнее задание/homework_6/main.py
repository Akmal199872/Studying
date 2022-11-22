import codecs
import random
import numpy

def IntroTask(number, textTask):
    print(f"\nЗадача №{number}\n")
    print(f'{textTask}\n')
def PrintArray():
    listArray = [random.randint(1, 9) for i in range(random.randint(3, 7))]
    return listArray


IntroTask(1, 'Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')

def UnevenSum(listArray):
    unevenSumArray = list(map(lambda x: x, listArray[1::2]))
    unevenSum = sum(unevenSumArray)
    print(listArray)
    print(unevenSum)

UnevenSum(PrintArray())

IntroTask(2, 'Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')

def MultiplyListNums(listArray):
    print(listArray)
    multiplArray = []
    i = 0
    while i < len(listArray) / 2:
        multiply = listArray[i] * listArray[len(listArray) - i - 1]
        multiplArray.append(multiply)
        i += 1
    print(list(enumerate(multiplArray)))

MultiplyListNums(PrintArray())

IntroTask(3, 'Напишите программу, которая будет преобразовывать десятичное число в двоичное')

def DecimalToBinary(listArray):
    decimalNums = list(zip(listArray, (map(lambda x: int(str(bin(x)[2:])), listArray))))
    print(listArray)
    print(decimalNums)

DecimalToBinary(PrintArray())

IntroTask(4, 'Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности')

def UniqueNumbers(listArray):
    uniqieNums = numpy.unique(listArray, return_index=True, return_inverse=False, return_counts=False)
    print(listArray)
    print(uniqieNums)

UniqueNumbers(PrintArray())

IntroTask(5, 'Напишите программу, удаляющую из текста все слова, содержащие "абв".')

def RemoveChars(fileName):
    with codecs.open(fileName, 'r', 'utf-8') as f:
        data = f.read()
        print(data)

    words = list(filter(lambda x: not x.casefold() == 'а' and not x.casefold() == 'б' and not x.casefold() == 'в', data))
    reply = "".join(words)
    print(reply)

RemoveChars('file.txt')