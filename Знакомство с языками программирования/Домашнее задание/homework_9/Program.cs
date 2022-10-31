void IntroTask(int number)
{
    System.Console.WriteLine($"{string.Empty}\nЗадача №{number}\n{string.Empty}");
}

// Задача №1

IntroTask(1);

int RecNumber(int number)
{
    if (number == 0)
    {
        return 0;
    }
    else
    {
        System.Console.WriteLine(number);
        return RecNumber(number - 1);
    }
}

RecNumber(8);

// Задача №2

IntroTask(2);

void RecTwoDigNumber(int number_1, int number_2, int result)
{
    if (number_1 > number_2) return;
    else
    {
        System.Console.WriteLine(result);
        RecTwoDigNumber(number_1: number_1 + 1, number_2: number_2, result: result + (number_1 + 1));
    }
}

RecTwoDigNumber(number_1: 4, number_2: 8, 4);

// Задача №3

IntroTask(3);

int Akkerman(int number_1, int number_2)
{
    if (number_1 == 0)
    {
        return number_2 + 1;
    }
    else
    {
        if ((number_1 != 0) && (number_2 == 0))
        {
            return Akkerman(number_1 - 1, 1);
        }
        else
        {
            return Akkerman(number_1 - 1, Akkerman(number_1, number_2 - 1));
        }
    }
}

System.Console.WriteLine(Akkerman(3, 2));