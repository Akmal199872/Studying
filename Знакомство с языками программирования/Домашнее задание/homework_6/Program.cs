// Задача №1

using System;
using System.Timers;
using System.Diagnostics;

System.Console.WriteLine("Задача №1");
System.Console.WriteLine();

void PrintArray(int [] array) {
    string string_array = string.Join(" ", array);
    System.Console.WriteLine($"Текущий массив: [ {string_array} ]");
}

void Timer() {
    var sw = new Stopwatch();
    sw.Start();
    
    int [] array = new int [1];
    int size = array.Length;
    int count = 0;
    Boolean situation = true;

    while (situation == true) {
        System.Console.Write("Введите любое число от 1 до 999: ");
        string input_number = Console.ReadLine();

        if (int.TryParse(input_number, out int number)) {
            System.Console.WriteLine($"Введено число = {number}");
            if (sw.ElapsedMilliseconds > 5000) {
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
            if (number > 0) {
                count++;
                System.Console.WriteLine($"Количество чисел больше нуля на данный момент = {count}.");
                System.Console.WriteLine();
            }
            else {
                System.Console.WriteLine($"Количество чисел больше нуля на данный момент = {count}.");
                System.Console.WriteLine();
            }
        }
        else {
            System.Console.WriteLine("Введено не число. Попробуйте ещё раз.");
            System.Console.WriteLine($"Прошло {sw.ElapsedMilliseconds} миллисекунд.");
            System.Console.WriteLine();
            sw.Restart();
        }
    }
}

// Timer();



// Задача №2

System.Console.WriteLine();
System.Console.WriteLine("Задача №2");
System.Console.WriteLine();

// y = k1 * x + b1, y = k2 * x + b2

