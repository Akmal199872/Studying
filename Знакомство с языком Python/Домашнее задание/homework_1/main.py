import math


def IntroTask(number):
    print("\nЗадача №", number, "\n")

IntroTask(1)

WeekDayNumber = int(input("Введите номер дня в неделе: "))

match WeekDayNumber:
    case 1:
        print("Это понедельник. Не выходной.")
    case 2:
        print("Это вторник. Не выходной.")
    case 3:
        print("Это среда. Не выходной.")
    case 4:
        print("Это четверг. Не выходной.")
    case 5:
        print("Это пятница. Не выходной.")
    case 6:
        print("Это суббота. Выходной!")
    case 7:
        print("Это воскресенье. Выходной!")

IntroTask(2)

for i in [True,False]:
    for j in [True, False]:
        for k in [True, False]:
            print(i, 'AND', j, 'OR', k, '=', i and j or k)

IntroTask(3)

CoordX = float(input("Введите координату x: "))
CoordY = float(input("Введите координату y: "))

if CoordX == 0 or CoordY == 0:
    print("Заданы неверные значения.")
elif CoordX > 0 and CoordY > 0:
    print("Точка будет находиться в плоскости 1")
elif CoordX < 0 and CoordY > 0:
    print("Точка будет находиться в плоскости 2")
elif CoordX < 0 and CoordY < 0:
    print("Точка будет находиться в плоскости 3")
elif CoordX > 0 and CoordY < 0:
    print("Точка будет находиться в плоскости 4")

IntroTask(4)

plane = int(input("Введите номер плоскости: "))

if plane == 1:
    print("Координата X > 0 и Координата Y > 0.")
elif plane == 2:
    print("Координата X < 0 и Координата Y > 0.")
elif plane == 3:
    print("Координата X < 0 и Координата Y < 0.")
elif plane == 4:
    print("Координата X > 0 и Координата Y < 0.")

IntroTask(5)


CoordXFirstPos = float(input("Введите координату x для первой точки: "))
CoordYFirstPos = float(input("Введите координату y для первой точки: "))

FirstPos = [CoordXFirstPos, CoordYFirstPos]

CoordXSecondPos = float(input("Введите координату x для второй точки: "))
CoordYSecondPos = float(input("Введите координату y для второй точки: "))

SecondPos = [CoordXSecondPos, CoordYSecondPos]

distance = math.sqrt(((SecondPos[0] - FirstPos[0]) ** 2) + ((SecondPos[1] - FirstPos[1]) ** 2))
print(round(distance, 2))