// Задача №1

using System;
using System.Timers;
using System.Diagnostics;

System.Console.WriteLine("Задача №1");
System.Console.WriteLine();

void PrintArray(int [] array) {
    string string_array = string.Join(" ", array);
    System.Console.WriteLine(string_array);
}

void Timer() {
    var sw = new Stopwatch();
    sw.Start();
    
    int [] array = new int [0];
    int size = array.Length;
    Boolean situation = true;

    while (situation == true) {
        System.Console.Write("Введите любое число от 1 до 999: ");
        string input_number = Console.ReadLine();

        if (int.TryParse(input_number, out int number)) {
            System.Console.WriteLine($"Введено число = {number}");
            if (sw.ElapsedMilliseconds > 5000) {
                System.Threading.Thread.Sleep(5000);
                System.Console.WriteLine("Программа завершилась");
                sw.Stop();
                situation = false;
            }
            System.Console.WriteLine($"Прошло {sw.ElapsedMilliseconds} миллисекунд.");
            System.Console.WriteLine();
            sw.Restart();
            size++;

            // Здесь написать код FillArray
            
            // for (int i = 0; i <= size; i++) {
            //     array[i] = number;
            //     PrintArray(array);
            // }

            System.Console.WriteLine($"Размер массива = {array.Length}");
        }
        else {
            System.Console.WriteLine("Введено не число. Попробуйте ещё раз.");
            System.Console.WriteLine($"Прошло {sw.ElapsedMilliseconds} миллисекунд.");
            System.Console.WriteLine();
            sw.Restart();
        }
    }
    
}

Timer();
