// Задача №1

void IntroTask(int number)
{
    System.Console.WriteLine($"{string.Empty}\nЗадача №{number}\n{string.Empty}");
}
Random rnd = new Random();
void PrintIntArray(int[,] array)
{
    System.Console.WriteLine("Массив:");
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            System.Console.Write($"{array[i, j]} ");
        }
        System.Console.WriteLine(string.Empty);
    }
}

int[,] FillIntArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = rnd.Next(1, 9);
        }
    }
    return array;
}

int[,] CreateArray()
{
    System.Console.WriteLine("Введите через пробел размеры массива: ");
    string[] StringInputNumbers = Console.ReadLine().Split();
    int RowSize = int.Parse(StringInputNumbers[0]);
    int ColumnSize = int.Parse(StringInputNumbers[1]);
    int[,] array = new int[RowSize, ColumnSize];
    return array;
}


IntroTask(1);

int[,] ChangeFirstLastRow()
{
    int[,] array = CreateArray();
    PrintIntArray(FillIntArray(array));

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[array.GetLength(0) - 1, j] = array[0, j];
        }
    }
    System.Console.WriteLine($"{string.Empty}\nОбновлённый массив\n{string.Empty}");
    PrintIntArray(array);
    return array;
}

// ChangeFirstLastRow();



// Задача №2

IntroTask(2);

int[] CopyColumn(int[,] array, int columnNumber)
{
    int[] column = new int[array.GetLength(1)];
    for (int i = 0; i < column.Length; i++)
    {
        column[i] = array[columnNumber, i];
    }
    return column;
}

void AddRowToArray(int[,] array, int[] row, int rowNumber)
{
    for (int i = 0; i < array.GetLength(1); i++)
    {
        array[rowNumber, i] = row[i];
    }
}

int[,] ChangeRowToColumn()
{
    int[,] array = CreateArray();
    PrintIntArray(FillIntArray(array));
    int[,] array_2 = new int[array.GetLength(1), array.GetLength(0)];

    for (int i = 0; i < array_2.GetLength(0); i++)
    {
        for (int j = 0; j < array_2.GetLength(1); j++)
        {
            array_2[i, j] = array[j, i];
        }
    }

    for (int i = 0; i < array.GetLength(0); i++)
    {
        int[] column = CopyColumn(array, i);
        AddRowToArray(array, column, i);
    }
    PrintIntArray(array_2);
    return array_2;
}



// ChangeRowToColumn();



// Задача №3

IntroTask(3);

int CountInputNumber()
{
    int[,] array = FillIntArray(CreateArray());
    PrintIntArray(array);
    int count = 0;
    int number = 0;
    bool issuccess = false;
    while (issuccess == false)
    {
        System.Console.Write("Введите число из массива: ");
        string inputNumber = Console.ReadLine();
        if (int.TryParse(inputNumber, out number))
        {
            count = 0;
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    if (number == array[i, j])
                    {
                        count++;
                    }
                }
            }
        }
        else
        {
            System.Console.WriteLine("Введено не число. Попробуйте ещё раз.");
            issuccess = false;
        }
        System.Console.WriteLine(string.Empty);
        System.Console.WriteLine($"Количество повторов числа {number} = {count}");
        System.Console.WriteLine(string.Empty);
    }
    return number;
}

// CountInputNumber();



// Задача №4

IntroTask(4);

int[,] CutRowColumnArray()
{
    int[,] array = FillIntArray(CreateArray());
    PrintIntArray(array);

    int min = array[0, 0];
    int min_x = 0;
    int min_y = 0;

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (array[i, j] < min)
            {
                min = array[i, j];
                min_x = i;
                min_y = j;
            }
        }
    }

    int [,] result_array = new int [array.GetLength(0) - 1, array.GetLength(1) - 1];

    for (int i = 0; i < result_array.GetLength(0); i++)
    {
        int m = 0;
        int n = 0;
        if (i != min_x)
        {
            m = 1;
        }

        for (int j = 0; j < result_array.GetLength(1); j++)
        {
            if (j == min_y)
            {
                n = 1;
            }
            
            result_array[i, j] = array[i + m, j + n];
            
            if (i == result_array.GetLength(0) - 1 && m != 1)
            {
                result_array[i, j] = array[i + m + 1, j + n];
            }

            if (j == result_array.GetLength(0) - 1 && n != 1)
            {
                result_array[i, j] = array[i + m, j + n + 1];
            }
        }
    }
    PrintIntArray(result_array);
    return result_array;
}

CutRowColumnArray();