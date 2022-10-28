// Первая задача

string input = Console.ReadLine();
Console.WriteLine(input);
int num = int.Parse(input);
int result = num * num;
Console.WriteLine(result);


// Вторая задача

Console.WriteLine("Введите первое число:");
string input1 = Console.ReadLine();
int num1 = int.Parse(input1);
Console.WriteLine("Введите второе число:");
string input2 = Console.ReadLine();
int num2 = int.Parse(input2);

int result = num1 * num1;
int div_num = result / num2;

if (div_num == num1)
{
    Console.WriteLine(div_num);
    Console.WriteLine("Делится!");
}
else
{
    Console.WriteLine(div_num);
    Console.WriteLine("Не делится!");
}

Третья задача
int num = int.Parse(Console.ReadLine());
Console.WriteLine("Введите номер дня в неделе:");

switch (num)
{
    case 1: Console.WriteLine("Monday"); break;
    case 2: Console.WriteLine("Tuesday"); break;
    case 3: Console.WriteLine("Wednesday"); break;
    case 4: Console.WriteLine("Thursday"); break;
}



// Четвёртая задача

Console.WriteLine("Введите число");
int num = int.Parse(Console.ReadLine());

int num_2 = num * (-1);

while (num_2 <= num)
{
    Console.WriteLine(num_2);
    num_2++;
}

Пятая задача

Console.WriteLine("Введите число");
string input = Console.ReadLine();

if (input.Length == 3)
{
    System.Console.WriteLine(input[input.Length - 1]);
}
else
{
    System.Console.WriteLine("Введите трёхзначное число");
}

