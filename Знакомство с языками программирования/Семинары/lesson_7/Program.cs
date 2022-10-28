// Задача №1
void PrintArray(int[] array)
{
    string string_array = string.Join(" ", array);
    System.Console.WriteLine($"Текущий массив: [ {string_array} ]");
}

System.Console.WriteLine("Задача №1");
System.Console.WriteLine();

int[] array_2 = new int[] { 1, 2, 3, 4 };

bool IsEven(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] % 2 == 0)
        {
            return true;
        }
    }
    return false;
}

if (!IsEven(array_2))
{
    System.Console.WriteLine(array_2[3]);
}



// Задача №2

System.Console.WriteLine();
System.Console.WriteLine("Задача №2");
System.Console.WriteLine();

int SizeArray()
{
    System.Console.Write($"Введите длину масcива №: ");
    string input_number = Console.ReadLine();
    if (int.TryParse(input_number, out int array_size)) return array_size;
    else System.Console.WriteLine("Введено не числовое значение. Повторите попытку.");
    return 0;
}

void PrintDoubleArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            System.Console.Write($"{array[i, j]} ");
        }
        System.Console.WriteLine();
    }
}
Random rnd = new Random();

int[,] CreateDoubleArray()
{
    int FirstSize = SizeArray();
    int SecondSize = SizeArray();
    int[,] array = new int[FirstSize, SecondSize];

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = rnd.Next(1, 9);
        }
    }
    return array;
}

PrintDoubleArray(CreateDoubleArray());



// Задача №3

System.Console.WriteLine();
System.Console.WriteLine("Задача №3");
System.Console.WriteLine();

int[,] CreateSumDoubleArray()
{
    int FirstSize = SizeArray();
    int SecondSize = SizeArray();
    int[,] array = new int[FirstSize, SecondSize];

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {

            array[i, j] = i + j;
        }
    }
    return array;
}

PrintDoubleArray(CreateSumDoubleArray());



// Задача №4

System.Console.WriteLine();
System.Console.WriteLine("Задача №4");
System.Console.WriteLine();

int[,] CreateEvenDoubleArray()
{
    int[,] array = CreateDoubleArray();
    System.Console.WriteLine("Начальная версия массива.");
    PrintDoubleArray(array);
    System.Console.WriteLine();
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if ((i - 1) % 2 == 0 && (j - 1) % 2 == 0 && i > 0 && j > 0)
            {
                array[i, j] = (int)Math.Pow(array[i, j], 2);
            }
        }
    }
    return array;
}
PrintDoubleArray(CreateEvenDoubleArray());



// Задача №5

System.Console.WriteLine();
System.Console.WriteLine("Задача №5");
System.Console.WriteLine();

int[,] DiagonalDoubleArrayNums()
{
    int result = 0;
    int[,] array = CreateDoubleArray();
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (i == j)
            {
                result += array[i, j];
                System.Console.WriteLine(result);
            }
        }
    }
    return array;
}

PrintDoubleArray(DiagonalDoubleArrayNums());