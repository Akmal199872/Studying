// Задача №1

using System;
using System.Timers;
using System.Diagnostics;

System.Console.WriteLine("Задача №1");
System.Console.WriteLine();
System.Console.WriteLine("Краткое описание задачи. Вам требуется вводить исключительно числа каждые 5 секунд, иначе доступ к вводу прекратится.");
System.Console.WriteLine("Количество чисел не ограничено. Ключевое в задаче: Покажет количество введённых чисел больше нуля.");
System.Console.WriteLine();

void PrintArray(int[] array)
{
    string string_array = string.Join(" ", array);
    System.Console.WriteLine($"Текущий массив: [ {string_array} ]");
}

void Timer()
{
    var sw = new Stopwatch();
    sw.Start();

    int[] array = new int[1];
    int size = array.Length;
    int count = 0;
    Boolean situation = true;

    while (situation == true)
    {
        System.Console.Write("Введите любое число от 1 до 999: ");
        string input_number = Console.ReadLine();

        if (int.TryParse(input_number, out int number))
        {
            System.Console.WriteLine($"Введено число = {number}");
            if (sw.ElapsedMilliseconds > 5000)
            {
                // System.Threading.Thread.Sleep(5000);
                System.Console.WriteLine($"Программа завершилась числом: {number}.");
                sw.Stop();
                situation = false;
            }
            System.Console.WriteLine($"Прошло {sw.ElapsedMilliseconds} миллисекунд.");
            // System.Console.WriteLine();
            sw.Restart();
            Array.Resize(ref array, size++);
            System.Console.WriteLine($"Размер массива = {array.Length}");
            array[size - 2] = number;
            PrintArray(array);
            if (number > 0)
            {
                count++;
                System.Console.WriteLine($"Количество чисел больше нуля на данный момент = {count}.");
                System.Console.WriteLine();
            }
            else
            {
                System.Console.WriteLine($"Количество чисел больше нуля на данный момент = {count}.");
                System.Console.WriteLine();
            }
        }
        else
        {
            System.Console.WriteLine("Введено не число. Попробуйте ещё раз.");
            System.Console.WriteLine($"Прошло {sw.ElapsedMilliseconds} миллисекунд.");
            System.Console.WriteLine();
            sw.Restart();
        }
    }
}

Timer();



// Задача №2

System.Console.WriteLine();
System.Console.WriteLine("Задача №2");
System.Console.WriteLine();
System.Console.WriteLine("Задача подразумевает вводить координаты отрезков. Программа позволит найти точки пересечения, указав координату.");

int RandomNumbers()
{

    int[] array = new int[1];
    int size = array.Length;

    double y;
    double x = 0.0;

    for (int i = 1; i <= 4; i++)
    {
        System.Console.Write($"Введите {i} значение для решения задачи: ");
        string input_number = Console.ReadLine();
        if (int.TryParse(input_number, out int number))
        {
            if (i < 3)
            {
                System.Console.WriteLine($"A{i} = {number}");
                Array.Resize(ref array, size++);
                array[size - 2] = number;
                PrintArray(array);
            }
            else
            {
                System.Console.WriteLine($"B{i - 2} = {number}");
                Array.Resize(ref array, size++);
                array[size - 2] = number;
                PrintArray(array);
            }
        }
        else
        {
            System.Console.WriteLine("Введено не число. Попробуйте ещё раз.");
            i--;
            System.Console.WriteLine();
        }
    }

    System.Console.WriteLine();
    PrintArray(array);
    System.Console.WriteLine($"Сформировано следующее уравнение: y = {array[0]}x + {array[2]}, y = {array[1]}x + {array[3]}");

    double[] array_2 = array.Select(z => Convert.ToDouble(z)).ToArray();

    if (array_2[0] == array_2[2] && array_2[1] == array_2[3])
    {
        System.Console.WriteLine("Прямые отрезки совпадают.");
    }
    else if (array_2[0] == array_2[2])
    {
        System.Console.WriteLine("Прямые отрезки расположены параллельно.");
    }
    else
    {
        x = -(array_2[2] - array_2[3]) / (array_2[0] - array_2[1]);
        string string_statement = ($"x = - ({array_2[2]} - {array_2[3]}) / ({array_2[0]} - {array_2[1]})");
        System.Console.WriteLine(string_statement);
        y = array_2[0] * (-(array_2[2] - array_2[3]) / (array_2[0] - array_2[1])) + array_2[2];

        System.Console.WriteLine($"Неизвестная x = {x}");
        System.Console.WriteLine($"Неизвестная y = {y}");
    }
    return 0;
}

RandomNumbers();
