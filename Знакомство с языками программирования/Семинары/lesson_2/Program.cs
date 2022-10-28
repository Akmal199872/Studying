// Задача №1
System.Console.WriteLine("Задача №1");
Random rnd = new Random();
int number = (int)rnd.NextInt64(10, 99);

System.Console.WriteLine(number);

int first_num = 0;
int second_num = 0;

first_num = number / 10;
second_num = number % 10;

System.Console.WriteLine(first_num + " " + second_num);

if (first_num > second_num)
{
    System.Console.WriteLine(first_num);
}
else
{
    System.Console.WriteLine(second_num);
}





// Задача №2

System.Console.WriteLine("");
System.Console.WriteLine("Задача №2");
// Random rnd = new Random();
int number_2 = (int)rnd.NextInt64(100, 999);

System.Console.WriteLine(number_2);
int first_d = number_2 / 100;
int third_d = number_2 % 10;

System.Console.WriteLine(first_d * 10 + third_d);

string number_3 = number_2.ToString();
System.Console.WriteLine(number_3[0] + "" + number_3[2]);





// Задача №3

System.Console.WriteLine("");
System.Console.WriteLine("Задача №3");
int number_4 = (int)rnd.Next(1, 99);
int number_5 = (int)rnd.Next(1, 9);

if (number_4 % number_5 == 0)
{
    System.Console.WriteLine(number_4 + " " + number_5);
}
else
{
    System.Console.WriteLine(number_4 + " " + number_5);
    System.Console.WriteLine("Не кратно");
    System.Console.WriteLine(number_4 % number_5);
}





// Задача №4

System.Console.WriteLine("");
System.Console.WriteLine("Задача №4");

int number_6 = (int)rnd.NextInt64(1, 999);

System.Console.WriteLine(number_6);

if (number_6 % 7 == 0 && number_6 % 23 == 0)
{
    System.Console.WriteLine("Число кратно");
}
else
{
    System.Console.WriteLine("Число некратно");
}





// Задача №5

System.Console.WriteLine("");
System.Console.WriteLine("Задача №5");

int number_7 = (int)rnd.NextInt64(1, 99);
System.Console.WriteLine(number_7);
System.Console.WriteLine("");
System.Console.WriteLine("Введите число от 1 до 100");
int number_8 = int.Parse(Console.ReadLine());

if (number_7 * number_7 == number_8)
{
    System.Console.WriteLine("Является квадратом");
}
else
{
    System.Console.WriteLine("Не является квадратом");
}
