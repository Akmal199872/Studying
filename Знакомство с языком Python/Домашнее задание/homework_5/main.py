import random


def IntroTask(number):
    print("\nЗадача №", number, "\n")


import codecs

IntroTask(1)

path = 'file.txt'
file = codecs.open(path, 'r', 'utf-8')
data = file.read() + ' '
file.close()

print(data)
words = list(filter(lambda x: not x.casefold() == 'а' and not x.casefold() == 'б' and not x.casefold() == 'в', data))
reply = "".join(words)
print(reply)

IntroTask(2)


def botVSbot():
    CandiesNumber = 2021
    CandiesNumberIndexFF = []
    CandiesNumberIndexSF = []

    FirstFriend = []
    SecondFriend = []

    FirstFriendCandiesNumber = 0
    SecondFriendCandiesNumber = 0
    i = 0
    index = []

    turn = random.randint(1, 2)
    if turn == 1:
        print("Начинает игрок 1")
        while CandiesNumber > 0:
            i += 1
            index.append(i)
            TakeNumber = random.randint(1, 28)

            FirstFriendCandiesNumber += TakeNumber
            FirstFriend.append(FirstFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexFF.append(CandiesNumber)
            FirstFriendData = list(zip(index, FirstFriend, CandiesNumberIndexFF))
            if CandiesNumber <= 0:
                break

            SecondFriendCandiesNumber += TakeNumber
            SecondFriend.append(SecondFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexSF.append(CandiesNumber)
            SecondFriedData = list(zip(index, SecondFriend, CandiesNumberIndexSF))
            if CandiesNumber <= 0:
                break
    else:
        print("Начинает игрок 2")
        while CandiesNumber > 0:
            i += 1
            index.append(i)
            TakeNumber = random.randint(1, 28)

            SecondFriendCandiesNumber += TakeNumber
            SecondFriend.append(SecondFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexSF.append(CandiesNumber)
            SecondFriedData = list(zip(index, SecondFriend, CandiesNumberIndexSF))
            if CandiesNumber <= 0:
                break

            TakeNumber = random.randint(1, 28)

            FirstFriendCandiesNumber += TakeNumber
            FirstFriend.append(FirstFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexFF.append(CandiesNumber)
            FirstFriendData = list(zip(index, FirstFriend, CandiesNumberIndexFF))
            if CandiesNumber <= 0:
                break

    print(f"\nРезультаты игрока 1: {FirstFriendData}")
    print(f"Результаты игрока 2: {SecondFriedData}")


botVSbot()

def playerVSplayer():
    CandiesNumber = 2021
    CandiesNumberIndexFF = []
    CandiesNumberIndexSF = []

    FirstFriend = []
    SecondFriend = []

    FirstFriendCandiesNumber = 0
    SecondFriendCandiesNumber = 0

    i = 0
    index = []

    turn = random.randint(1, 2)
    if turn == 1:
        print("Начинает игрок 1")
        while CandiesNumber > 0:
            i += 1
            index.append(i)
            TakeNumber = int(input(f"Игрок №1 возьмёт конфет = "))
            if TakeNumber < 0 or TakeNumber > 28:
                print("Взял неверное количество конфет.")
                TakeNumber = int(input("Попробуй взять ещё раз."))
            FirstFriendCandiesNumber += TakeNumber
            FirstFriend.append(FirstFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexFF.append(CandiesNumber)
            FirstFriendData = list(zip(index, FirstFriend, CandiesNumberIndexFF))
            if CandiesNumber <= 0:
                break

            TakeNumber = int(input(f"Игрок №2 возьмёт конфет = "))
            if TakeNumber < 0 or TakeNumber > 28:
                print("Взял неверное количество конфет.")
                TakeNumber = int(input("Попробуй взять ещё раз."))
            SecondFriendCandiesNumber += TakeNumber
            SecondFriend.append(SecondFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexSF.append(CandiesNumber)
            SecondFriendData = list(zip(index, SecondFriend, CandiesNumberIndexSF))
            if CandiesNumber <= 0:
                break
    else:
        print("Начинает игрок 2")
        while CandiesNumber > 0:
            i += 1
            index.append(i)
            TakeNumber = int(input(f"Игрок №2 возьмёт конфет = "))
            if TakeNumber < 0 or TakeNumber > 28:
                print("Взял неверное количество конфет.")
                TakeNumber = int(input("Попробуй взять ещё раз."))
            SecondFriendCandiesNumber += TakeNumber
            SecondFriend.append(SecondFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexSF.append(CandiesNumber)
            SecondFriendData = list(zip(index, SecondFriend, CandiesNumberIndexSF))
            if CandiesNumber <= 0:
                break

            TakeNumber = int(input(f"Игрок №1 возьмёт конфет = "))
            if TakeNumber < 0 or TakeNumber > 28:
                print("Взял неверное количество конфет.")
                TakeNumber = int(input("Попробуй взять ещё раз."))
            FirstFriendCandiesNumber += TakeNumber
            FirstFriend.append(FirstFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexFF.append(CandiesNumber)
            FirstFriendData = list(zip(index, FirstFriend, CandiesNumberIndexFF))
            if CandiesNumber <= 0:
                break

    print(f"\nРезультаты игрока 1: {FirstFriendData}")
    print(f"Результаты игрока 2: {SecondFriendData}")


playerVSplayer()

def playerVSbot():
    CandiesNumber = 2021
    CandiesNumberIndexFF = []
    CandiesNumberIndexSF = []

    FirstFriend = []
    SecondFriend = []

    FirstFriendCandiesNumber = 0
    SecondFriendCandiesNumber = 0

    i = 0
    index = []

    turn = random.randint(1, 2)
    if turn == 1:
        print("Начинает игрок 1")
        while CandiesNumber > 0:
            i += 1
            index.append(i)
            TakeNumber = int(input(f"Игрок №1 возьмёт конфет = "))
            if TakeNumber < 0 or TakeNumber > 28:
                print("Взял неверное количество конфет.")
                TakeNumber = int(input("Попробуй взять ещё раз."))
            FirstFriendCandiesNumber += TakeNumber
            FirstFriend.append(FirstFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexFF.append(CandiesNumber)
            FirstFriendData = list(zip(index, FirstFriend, CandiesNumberIndexFF))
            if CandiesNumber <= 0:
                break

            TakeNumber = random.randint(1, 28)
            print(f"Игрок №2 возьмёт конфет = {TakeNumber}")

            SecondFriendCandiesNumber += TakeNumber
            SecondFriend.append(SecondFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexSF.append(CandiesNumber)
            SecondFriendData = list(zip(index, SecondFriend, CandiesNumberIndexSF))
            if CandiesNumber <= 0:
                break
    else:
        print("Начинает игрок 2")
        while CandiesNumber > 0:
            i += 1
            index.append(i)

            TakeNumber = random.randint(1, 28)
            print(f"Игрок №2 возьмёт конфет = {TakeNumber}")

            SecondFriendCandiesNumber += TakeNumber
            SecondFriend.append(SecondFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexSF.append(CandiesNumber)
            SecondFriendData = list(zip(index, SecondFriend, CandiesNumberIndexSF))
            if CandiesNumber <= 0:
                break

            TakeNumber = int(input(f"Игрок №1 возьмёт конфет = "))
            if TakeNumber < 0 or TakeNumber > 28:
                print("Взял неверное количество конфет.")
                TakeNumber = int(input("Попробуй взять ещё раз."))
            FirstFriendCandiesNumber += TakeNumber
            FirstFriend.append(FirstFriendCandiesNumber)
            CandiesNumber -= TakeNumber
            CandiesNumberIndexFF.append(CandiesNumber)
            FirstFriendData = list(zip(index, FirstFriend, CandiesNumberIndexFF))
            if CandiesNumber <= 0:
                break

    print(f"\nРезультаты игрока 1: {FirstFriendData}")
    print(f"Результаты игрока 2: {SecondFriendData}")


playerVSbot()


IntroTask(3)


def TicTacToe():

    maps = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]

    victories = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]

    def print_maps():
        print(maps[0], end=" ")
        print(maps[1], end=" ")
        print(maps[2])

        print(maps[3], end=" ")
        print(maps[4], end=" ")
        print(maps[5])

        print(maps[6], end=" ")
        print(maps[7], end=" ")
        print(maps[8])

    def step_maps(step, symbol):
        ind = maps.index(step)
        maps[ind] = symbol

    def get_result():
        win = ""

        for i in victories:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                win = "X"
            if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
                win = "O"

        return win

    game_over = False
    player1 = True

    while game_over == False:

        print_maps()

        if player1 == True:
            symbol = "X"
            step = int(input("Человек 1, ваш ход: "))
        else:
            symbol = "O"
            step = int(input("Человек 2, ваш ход: "))

        step_maps(step, symbol)
        win = get_result()
        if win != "":
            game_over = True
        else:
            game_over = False

        player1 = not (player1)

    print_maps()
    print("Победил", win)


TicTacToe()


IntroTask(4)

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

path1 = 'input.txt'
path2 = 'output.txt'
FileInput = open(path1, 'r')
DataNew = FileInput.read() + ' '
FileInput.close()

FileOutput = open(path2, 'w')
DataNew2 = FileOutput.write(rle_encode(DataNew))
FileOutput.close()

print(rle_encode(DataNew))


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

FileInput = open(path2, 'r')
DataNew = FileInput.read() + ' '
FileInput.close()


FileOutput = open(path1, 'w')
DataNew2 = FileOutput.write(rle_decode(DataNew))
FileOutput.close()

print(rle_decode(DataNew))