void IntroTask(int number)
{
    System.Console.WriteLine($"{string.Empty}\nЗадача №{number}\n{string.Empty}");
}

// Задача №1

IntroTask(1);

void RecNumber(int number)
{
    if (number == 1) 
    {
        System.Console.WriteLine(number);
        return;
    }
    else
    {
        System.Console.WriteLine(number);
        RecNumber(number - 1);
    }
}

RecNumber(5);

// Задача №2

IntroTask(2);

void RecTwoDigNumber(int number_1, int number_2)
{
    if (number_1 > number_2) return;
    else
    {
        System.Console.WriteLine(number_1);
        RecTwoDigNumber(number_1 + 1, number_2);
    }
}

RecTwoDigNumber(1, 12);

// Задача №3

IntroTask(3);

int StringSum(int number)
{
    if (number / 10 == 0)
    {
        return number;
    }
    else
    {
        return StringSum(number / 10) + number % 10;
    }
}

System.Console.WriteLine(StringSum(133));

// Задача №4

IntroTask(4);

int PowNumber(int number_1, int number_2)
{
    if (number_2 == 1)
    {
        return number_1;
    }
    else
    {
        return PowNumber(number_1,number_2 - 1)*number_1;
    }
}

System.Console.WriteLine(PowNumber(3, 5));