// Задача №19

System.Console.WriteLine("Задача №19");
System.Console.WriteLine("");

int result = 0;

while (true)
{
    System.Console.Write("Ввведите число 'палиндром': ");
    int number_1 = int.Parse(Console.ReadLine());

    string s_number_1 = number_1.ToString();
    int size_1 = s_number_1.Length;
    int count_1 = 1;

    if (s_number_1[count_1 - 1] == s_number_1[size_1 - 1])
    {
        count_1++;
        result = number_1;
        break;
    }
    else
    {
        System.Console.WriteLine("Число не является палиндромом. Введите число заново.");
    }
}
System.Console.WriteLine($"Число, которое является палиндромом равно: {result}");





// Задача №21

System.Console.WriteLine("");
System.Console.WriteLine("Задача №21");
System.Console.WriteLine("");

int[,] array_1 = new int[3, 3];
Random rnd = new Random();

int random_num(int min_value, int max_value)
{
    int random_number_1 = rnd.Next(min_value, max_value);
    System.Console.WriteLine($"Загаданное число равно: {random_number_1}");
    return random_number_1;
}

array_1[0, 0] = random_num(1, 9);
array_1[0, 1] = random_num(1, 9);
array_1[1, 0] = random_num(1, 9);
array_1[1, 1] = random_num(1, 9);
array_1[2, 1] = random_num(1, 9);
array_1[2, 2] = random_num(1, 9);

double result_pow = Math.Pow((Math.Pow(array_1[0, 0] - array_1[1, 0], 2)) + (Math.Pow(array_1[0, 1] - array_1[1, 1], 2)) + (Math.Pow(array_1[1, 2] - array_1[2, 2], 2)), 2);
double result_sqrt = Math.Sqrt(result_pow);

System.Console.Write($"Результат поиска расстояния равен: {result_sqrt}");





// Задача №23
// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.

// 3 -> 1, 8, 27
// 5 -> 1, 8, 27, 64, 125

System.Console.WriteLine("");
System.Console.WriteLine("Задача №23");
System.Console.WriteLine("");

System.Console.Write("Введите любое число для вычисления кубов: ");
int size_2 = int.Parse(Console.ReadLine());

for (int i = 1; i <= size_2; i++)
{
    double result_3 = Math.Pow(i, 3);
    System.Console.WriteLine($"Куб числа {i} равен: {result_3}");
}