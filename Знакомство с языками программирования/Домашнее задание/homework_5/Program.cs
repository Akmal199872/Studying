// Задача №1

System.Console.WriteLine("Задача №1");
System.Console.WriteLine();

Random rnd = new Random();

int [] CreateArray(int minValue, int maxValue) {
    System.Console.Write("Введите размер массива: ");
    int count = int.Parse(Console.ReadLine());
    int [] array = new int [count];
    for (int i = 0; i < count; i++) {
        array[i] = rnd.Next(minValue, maxValue);
    }
    return array;
}

void PrintArray(int [] array) {
    string string_array = string.Join(" ", array);
    System.Console.WriteLine(string_array);
}

int EvenNumberInArray(int [] array) {
    PrintArray(array);
    int count = 0;
    for (int i = 0; i < array.Length; i++) {
        if (array[i] % 2 == 0) {
            // System.Console.WriteLine($"Число {array[i]} является чётным");
            count++;
        }
    }
    System.Console.WriteLine($"Количество чётных чисел в массиве = {count}");
    return count;
}

EvenNumberInArray(CreateArray(100, 999));





// Задача №2

System.Console.WriteLine();
System.Console.WriteLine("Задача №2");
System.Console.WriteLine();

int NotEvenNumberSumInArray(int [] array) {
    PrintArray(array);
    int result = 0;
    for (int i = 0; i < array.Length; i++) {
        if (i % 2 != 0) {
            // System.Console.WriteLine($"{i} элемент массива = {array[i]}");
            result = result + array[i];
        }
    }
    System.Console.WriteLine($"Сумма всех нечётных элементов массива: {result}");
    return result;
}

NotEvenNumberSumInArray(CreateArray(1, 9));





// Задача №3

System.Console.WriteLine();
System.Console.WriteLine("Задача №3");
System.Console.WriteLine();

double [] CreateArrayDouble() {
    System.Console.Write("Введите размер массива: ");
    int count = int.Parse(Console.ReadLine());
    double [] array = new double [count];
    for (int i = 0; i < count; i++) {
        array[i] = rnd.NextDouble() * 100;
    }
    string string_array = string.Join(" ", array);
    System.Console.WriteLine(string_array);
    return array;
}

double SearchDiffMinMaxValue(double [] array) {
    double result = 0;
    int size = array.Length;
    double max = -1.0;
    double min = array[0];
    int index = -1;
    int index_2 = 0;    

    for (int i = 0; i < size; i++) {
        if (max <= array[i]) {
            max = array[i];
            index = i;
        }
        else if (min >= array[i]) {
            min = array[i];
            index_2 = i;
        }
    }
    System.Console.WriteLine($"Наибольшее число в массиве: {max}");
    System.Console.WriteLine($"Индекс наибольшего числа: {index}");

    System.Console.WriteLine($"Наименьшее число в массиве: {min}");
    System.Console.WriteLine($"Индекс наименьшего числа: {index_2}");
    result = max - min;
    System.Console.WriteLine($"Разница между наибольшим и наименьшим элементов в массиве = {result}");
    return result;  
}

SearchDiffMinMaxValue(CreateArrayDouble());