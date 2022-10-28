// Задача №1

void Method1()
{
    System.Console.WriteLine("Я ничего не принимаю и не возвращаю!");
}

Method1();



// Задача №2

void Method2(string msg_1)
{
    System.Console.WriteLine($"{msg_1}");
}

Method2("Я принимаю аргументы!");



// Задача №3

void Method3(string msg_2, int count_1)
{
    int i = 0;
    while (i <= count_1)
    {
        System.Console.WriteLine(msg_2);
        i++;
    }
}

Method3("Я принимаю аргументы четыре раза!", 4);
Method3(count_1: 3, msg_2: "В обратном порядке");



// Задача №4

int Method4()
{
    return DateTime.Now.Year;
}

int year = Method4();
System.Console.WriteLine($"Текущий год: {year}");



// Задача №5

string Method5(int count_2, string text_1)
{
    int i = 0;
    string result_1 = String.Empty;
    while (i < count_2)
    {
        result_1 = result_1 + text_1;
        i++;
    }
    return result_1;
}

string result = Method5(10, "z");
System.Console.WriteLine(result);



// Задача №6

string Method6(int count_3, string text_2)
{
    string result = string.Empty;
    for (int i = 0; i < count_3; i++)
    {
        result = result + text_2;
    }
    return result;
}

string result_2 = Method6(10, "z");
System.Console.WriteLine(result_2);



// Задача №7

for (int i = 2; i <= 10; i++)
{
    for (int j = 0; j <= 10; j++)
    {
        System.Console.WriteLine($"{i} * {j} = {i * j}");
    }
    System.Console.WriteLine("");
}



// Задача №8

string text_3 = "- Я думаю, - сказал князь, улыбаясь, - что, "
                + "ежели бы вас послали вместо нашего милого Винценгероде,"
                + "вы бы взяли приступом согласие прусского короля. "
                + "Вы так красноречивы. Вы дадите мне чаю?";

string Replace(string text, char oldValue, char newValue)
{
    string result_3 = string.Empty;
    int length = text_3.Length;
    for (int i = 0; i < length; i++)
    {
        if (text_3[i] == oldValue)
        {
            result_3 = result_3 + $"{newValue}";
            System.Console.WriteLine(result_3);
        }
        else
        {
            result_3 = result_3 + $"{text[i]}";
            System.Console.WriteLine(result_3);
        }
    }
    return result_3;
}

string newText_1 = Replace(text_3, ' ', '|');
System.Console.WriteLine(newText_1);



// Задача №9

int[] array = { 1, 5, 3, 4, 3, 6, 7, 2 };

void PrintArray(int[] array)
{
    int count_4 = array.Length;
    for (int i = 0; i < count_4; i++)
    {
        System.Console.WriteLine($"{array[i]}");
    }
    System.Console.WriteLine("");
}

void SelectionSort(int[] array)
{
    for (int i = 0; i < array.Length - 1; i++)
    {
        int minPosition = i;
        for (int j = i + 1; j < array.Length; j++)
        {
            if (array[j] < array[minPosition])
            {
                minPosition = j;
            }
        }
        int temporary = array[i];
        array[i] = array[minPosition];
        array[minPosition] = temporary;
    }
}

PrintArray(array);
SelectionSort(array);
PrintArray(array);
