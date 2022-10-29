// Задача №1

System.Console.WriteLine("Задача №1");
System.Console.WriteLine();

Random rnd = new Random();

void PrintDoubleArray(double [,] array)
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

double [,] CreateDoubleTwoDimensionArray()
{
    System.Console.Write("Введите размеры массива через пробел: ");
    string [] StringInputNumbers = Console.ReadLine().Split();
    int RowSize = int.Parse(StringInputNumbers[0]);
    int ColumnSize = int.Parse(StringInputNumbers[1]);
    double [,] array = new double [RowSize, ColumnSize];

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = rnd.NextDouble();
            array[i, j] = Math.Round(array[i,j], 2);
        }
    }

    return array;
}

PrintDoubleArray(CreateDoubleTwoDimensionArray());





// Задача №2

System.Console.WriteLine();
System.Console.WriteLine("Задача №2");
System.Console.WriteLine();

int [,] CreateIntTwoDimensionArray()
{
    System.Console.Write("Введите размеры массива через пробел: ");
    string [] StringInputNumbers = Console.ReadLine().Split();
    int RowSize = int.Parse(StringInputNumbers[0]);
    int ColumnSize = int.Parse(StringInputNumbers[1]);
    int [,] array = new int [RowSize, ColumnSize];

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = rnd.Next(1,9);
        }
    }
        
    return array;
}

void PrintIntArray(int [,] array)
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

int SearchInt()
{
    int [,] array = CreateIntTwoDimensionArray();
    PrintIntArray(array);
    int number = 0;

    while (true)
    {
        System.Console.Write("Введите координаты массива через пробел: ");
        string [] StringInputNumbers = Console.ReadLine().Split();
        int RowSize = int.Parse(StringInputNumbers[0]);
        int ColumnSize = int.Parse(StringInputNumbers[1]);

        try
        {
            number = array[RowSize, ColumnSize];
            System.Console.WriteLine(number);
            break;
        }
        catch (IndexOutOfRangeException)
        {
            System.Console.WriteLine("Такого числа в массиве нет");
            continue;
        }
    }

    return number;
}

SearchInt();





// Задача №3

System.Console.WriteLine();
System.Console.WriteLine("Задача №3");
System.Console.WriteLine();

double AverageColumn()
{
    int RowSize = rnd.Next(1,9);
    int ColumnSize = rnd.Next(1,9);
    int [,] array = new int [RowSize, ColumnSize];
    double result = 0;
    double ColumnSum = 0;

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i,j] = rnd.Next(1,9);
        }
    }
    System.Console.WriteLine("Массив:");
    PrintIntArray(array);

    for (int j = 0; j < array.GetLength(1); j++)
    {
        ColumnSum = 0;
        for (int i = 0; i < array.GetLength(0); i++)
        {
            ColumnSum += array[i,j];
        }
        result = Math.Round(ColumnSum / array.GetLength(0), 2);
        System.Console.WriteLine($"Результат столбца №{j + 1} = {result}");
    }
    return result;
}

AverageColumn();