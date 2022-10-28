// Задача №1

System.Console.WriteLine("Задача №1");
System.Console.WriteLine();

System.Console.Write("Введите размер массива: ");

int number_1 = int.Parse(Console.ReadLine());
int[] array_1 = new int[number_1];

void FillArray(int[] array, int minValue, int maxValue)
{
    for (int i = 0; i < array.Length; i++)
    {
        Random rnd = new Random();
        int random_num = rnd.Next(minValue, maxValue);
        array[i] = random_num;
        // System.Console.WriteLine($"Случайное число в массиве №{i + 1} = {random_num}");
    }
    PrintArray(array);
}

int PositiveSum(int[] array)
{
    int result = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] > 0)
        {
            result = result + array[i];
        }
    }
    System.Console.WriteLine($"Результат суммы положительных чисел: {result}");
    return result;
}

int NegativeSum(int[] array)
{
    int result = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] < 0)
        {
            result = result + array[i];
        }
    }
    System.Console.WriteLine($"Результат суммы отрицательных чисел: {result}");
    return result;
}

FillArray(array_1, -9, 9);
PositiveSum(array_1);
NegativeSum(array_1);




// Задача №2

System.Console.WriteLine();
System.Console.WriteLine("Задача №2");
System.Console.WriteLine();

int[] array_2 = new int[number_1];

void PrintArray(int[] array)
{
    string string_array = string.Join(" ", array);
    System.Console.WriteLine(string_array);
}

void InvertNumber(int[] array, int[] array_2)
{
    for (int i = 0; i < array.Length; i++)
    {
        int result = array[i] * -1;
        // System.Console.WriteLine($"Результат №{i + 1}: {result}");
        array_2[i] = result;
    }
    PrintArray(array_2);
}

System.Console.WriteLine();
FillArray(array_1, -9, 9);
InvertNumber(array_1, array_2);




// Задача №3

System.Console.WriteLine();
System.Console.WriteLine("Задача №3");
System.Console.WriteLine();

System.Console.Write("Введите число, которое может быть в массиве: ");
int number_2 = int.Parse(Console.ReadLine());

for (int i = 0; i < array_1.Length; i++)
{
    if (number_2 == array_1[i] || number_2 * (-1) == array_1[i])
    {
        System.Console.WriteLine($"В массиве присутствует число: {number_2}. Поиск завершился на {i + 1} итерации.");
        break;
    }
    else
    {
        System.Console.WriteLine($"Введённое число не равно {i} элементу массива.");
    }
}

PrintArray(array_1);


// int c = (int)Console.ReadKey().KeyChar;

// Задача №4

System.Console.WriteLine();
System.Console.WriteLine("Задача №4");
System.Console.WriteLine();

int[] array_3 = new int[123];

void SearchNumberRange(int[] array, int minValue, int maxValue)
{
    int result = 0;
    FillArray(array_3, 1, 1000);
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] >= minValue && array[i] <= maxValue)
        {
            int count = 1;
            result = result + count;
            count++;
            System.Console.WriteLine($"Число в диапазоне = {array[i]}");
        }
    }
    System.Console.WriteLine($"Количество найденных чисел в диапазоне: {result}");
}

SearchNumberRange(array_3, 10, 99);



// Задача №5

System.Console.WriteLine();
System.Console.WriteLine("Задача №5");
System.Console.WriteLine();

void MultiplyNumbers(int[] array, int minValue, int maxValue)
{
    FillArray(array, minValue, maxValue);
    int size = array.Length;
    int i = 0;
    int result = 0;
    int[] array_2 = new int[(size / 2) + 1];
    while (i < size)
    {
        // System.Console.WriteLine($"Первый элемент массива = {array[i]}. Последний элемент массива = {array[size - 1]}");
        result = array[i] * array[size - 1];
        i++;
        size--;
        array_2[i - 1] = result;
    }
    System.Console.WriteLine("Массив из произведений:");
    PrintArray(array_2);
}

MultiplyNumbers(array_3, 1, 9);

