void IntroTask(int number)
{
    System.Console.WriteLine($"{string.Empty}\nЗадача №{number}\n{string.Empty}");
}

int RandomNumbers()
{
    return new Random().Next(1, 9);
}

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
            array[i, j] = RandomNumbers();
        }
    }
    return array;
}

int[,] CreateArray()
{
    System.Console.Write("Введите через пробел размеры массива: ");
    string[] StringInputNumbers = Console.ReadLine().Split();
    int RowSize = int.Parse(StringInputNumbers[0]);
    int ColumnSize = int.Parse(StringInputNumbers[1]);
    int[,] array = new int[RowSize, ColumnSize];
    return array;
}

// Задача №1

IntroTask(1);

int[,] SortBiggetsToSmallest()
{
    int[,] array = FillIntArray(CreateArray());
    PrintIntArray(array);

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1) - 1; j++)
        {
            for (int m = 0; m < array.GetLength(1) - 1; m++)
            {
                if (array[i, m] < array[i, m + 1])
                {
                    int temp = 0;
                    temp = array[i, m];
                    array[i, m] = array[i, m + 1];
                    array[i, m + 1] = temp;
                }
            }
        }
    }

    PrintIntArray(array);
    return array;
}

// SortBiggetsToSmallest();



// Задача №2

IntroTask(2);

int[,] SumRowArray()
{
    int[,] array = FillIntArray(CreateArray());
    PrintIntArray(array);
    int[] tempArray = new int[0];


    for (int i = 0; i < array.GetLength(0); i++)
    {
        int result = 0;
        for (int j = 0; j < array.GetLength(1); j++)
        {
            result += array[i, j];
        }
        System.Console.WriteLine($"Сумма {i + 1} строки = {result}");
        Array.Resize(ref tempArray, tempArray.Length + 1);
        tempArray[i] = result;
    }

    int min = tempArray[0];
    int index = 0;

    for (int i = 1; i < tempArray.Length; i++)
    {
        if (min > tempArray[i])
        {
            min = tempArray[i];
            index = i;
        }
    }

    System.Console.WriteLine($"Сумма {index + 1} строки является наименьшей");


    return array;
}

// SumRowArray();



// Задача №3

IntroTask(3);
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

int[,] MultiplyMatrix()
{
    int[,] ResultArray = new int[0, 0];
    bool issuccess = false;
    while (issuccess == false)
    {
        try
        {
            int[,] array_1 = FillIntArray(CreateArray());
            PrintIntArray(array_1);
            int[,] array_2 = FillIntArray(CreateArray());
            PrintIntArray(array_2);

            int[,] array_21 = new int[array_2.GetLength(0), array_2.GetLength(1)];

            ResultArray = new int[array_1.GetLength(0), array_1.GetLength(1)];

            for (int i = 0; i < array_2.GetLength(0); i++)
            {
                for (int j = 0; j < array_2.GetLength(1); j++)
                {
                    array_21[i, j] = array_2[j, i];
                }
            }

            for (int i = 0; i < ResultArray.GetLength(0); i++)
            {
                for (int j = 0; j < ResultArray.GetLength(1); j++)
                {
                    ResultArray[i, j] = 0;
                    for (int m = 0; m < ResultArray.GetLength(1); m++)
                    {
                        ResultArray[i, j] += array_1[i, m] * array_2[m, j];
                    }
                }
            }

            PrintIntArray(ResultArray);
            issuccess = true;
        }

        catch (IndexOutOfRangeException)
        {
            System.Console.WriteLine("Указан разный размер массивов. Попробуйте ещё раз.");
            issuccess = false;
        }
    }
    return ResultArray;
}

// MultiplyMatrix();



// Задача №4

int[,,] CreateThreeDimArray()
{
    System.Console.WriteLine("Введите через пробел размеры массива: ");
    string[] StringInputNumbers = Console.ReadLine().Split();
    int XSize = int.Parse(StringInputNumbers[0]);
    int YSize = int.Parse(StringInputNumbers[1]);
    int ZSize = int.Parse(StringInputNumbers[2]);
    int[,,] array = new int[XSize, YSize, ZSize];
    return array;
}

int[,,] FillThreeDimArray(int[,,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int m = 0; m < array.GetLength(2); m++)
            {
                array[i, j, m] = RandomNumbers();
            }
        }
    }
    return array;
}

int[,,] PrintThreeDimArray(int[,,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int m = 0; m < array.GetLength(2); m++)
            {
                System.Console.Write($"{array[i, j, m]} ");
            }
        }
        System.Console.WriteLine(string.Empty);
    }
    return array;
}

IntroTask(4);

int[,,] FillThreeDimUniqueArray()
{
    int[,,] array = FillThreeDimArray(CreateThreeDimArray());
    PrintThreeDimArray(array);

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int m = 0; m < array.GetLength(2); m++)
            {
                while (array[i, j, m] == 0)
                {
                    int number = RandomNumbers();
                    if (array[i, j, m] == number)
                    {
                        array[i, j, m] = RandomNumbers();
                    }
                }
            }
        }
    }
    return array;
}

// FillThreeDimUniqueArray();



// Задача №5

IntroTask(5);

int[,] SpiralArray()
{
    int[,] array = CreateArray();
    PrintIntArray(array);

    int number = 1;
    int i = 0;
    int j = 0;

    while (number <= array.GetLength(0) * array.GetLength(1))
    {
        array[i, j] = number;
        if (i <= j + 1 && i + j < array.GetLength(1) - 1)
        {
            j++;
        }
        else if (i < j && i + j >= array.GetLength(0) - 1)
        {
            i++;
        }
        else if (i >= j && i + j > array.GetLength(1) - 1)
        {
            j--;
        }
        else
        {
            i--;
        }
        number++;
    }
    PrintIntArray(array);
    return array;
}

// SpiralArray();



// Задача №6

IntroTask(6);

int[,] PascalTriange()
{
    int[,] array = CreateArray();
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = 0;
        }
    }
    for (int i = 0; i < array.GetLength(0); i++)
    {
        array[i, 0] = 1;
        array[i, i] = 1;
    }
    for (int i = 2; i < array.GetLength(0); i++)
    {
        for (int j = 1; j < i; j++)
        {
            array[i, j] = array[i - 1, j - 1] + array[i - 1, j];
        }
    }
    PrintIntArray(array);
    return array;
}

PascalTriange();