// Задача №10

System.Console.WriteLine("Задача №10");
System.Console.WriteLine("");

Random rnd = new Random();
int number_1 = (int)rnd.NextInt64(100, 999);
string s_number_1 = number_1.ToString();
System.Console.WriteLine($"Изначальное число: {number_1}");
System.Console.WriteLine($"Результат: {s_number_1[1]}");




// Задача №13

System.Console.WriteLine("");
System.Console.WriteLine("Задача №13");
System.Console.WriteLine("");

System.Console.WriteLine("Введите трёхзначное число:");

while (true)
{
    int number_2 = int.Parse(s: Console.ReadLine());
    string s_number_2 = number_2.ToString();
    if (s_number_2.Length >= 3)
    {
        System.Console.WriteLine(s_number_2[2]);
        break;
    }
    else
    {
        System.Console.WriteLine("Нет третьей цифры. Введите число заново.");
    }
}





// Задача №15

System.Console.WriteLine("");
System.Console.WriteLine("Задача №15");
System.Console.WriteLine("");

for (int i = 0; i < 3; i++)
{
    System.Console.WriteLine("Укажите номер дня недели:");
    int number_3 = int.Parse(Console.ReadLine());

    switch (number_3)
    {
        case 1:
            {
                System.Console.WriteLine("Понедельник. Не является выходным днём");
                break;
            }
        case 2:
            {
                System.Console.WriteLine("Вторник. Не является выходным днём");
                break;
            }
        case 3:
            {
                System.Console.WriteLine("Среда. Не является выходным днём");
                break;
            }
        case 4:
            {
                System.Console.WriteLine("Четверг. Не является выходным днём");
                break;
            }
        case 5:
            {
                System.Console.WriteLine("Пятница. Не является выходным днём");
                break;
            }
        case 6:
            {
                System.Console.WriteLine("Суббота. Выходной!");
                break;
            }
        case 7:
            {
                System.Console.WriteLine("Воскресенье. Выходной!");
                break;
            }
    }
}
