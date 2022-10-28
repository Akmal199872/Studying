// Задача №25

System.Console.WriteLine("Задача №25");
System.Console.WriteLine("");

System.Console.Write("Введите первое число: ");
int number_1 = int.Parse(Console.ReadLine());
System.Console.Write("Введите второе число: ");
int number_2 = int.Parse(Console.ReadLine());

void pow_cycle(int number_1, int number_2)
{
    int result = 1;
    for (int i = 1; i <= number_2; i++)
    {
        result = result * number_1;
        System.Console.WriteLine($"Результат возведения в {i} степень числа {number_1}: {result}");
    }
}

pow_cycle(number_1, number_2);




// Задача №27

System.Console.WriteLine("");
System.Console.WriteLine("Задача №27");
System.Console.WriteLine("");

Random rnd = new Random();
int number_3 = rnd.Next(1, 999);

void string_sum(int number_4)
{
    int result = 0;
    System.Console.WriteLine($"Заданное число равно: {number_4}");
    string s_number_4 = number_4.ToString();
    int size = s_number_4.Length;

    for (int i = 0; i < size; i++)
    {
        int number_5 = int.Parse(s_number_4[i].ToString());
        System.Console.WriteLine($"{result} = {result} + {number_5}");
        System.Console.WriteLine($"Значение {i} элемента массива: {number_5}");
        result = result + number_5;
        System.Console.WriteLine($"Результатом суммы будет: {result}");
    }
    System.Console.WriteLine($"Сумма цифр числа {number_4} равна {result}");
}

string_sum(number_3);




// Задача №29

System.Console.WriteLine("");
System.Console.WriteLine("Задача №29");
System.Console.WriteLine("");

int random_num()
{
    int number = new Random().Next(1, 99);
    return number;
}

int[] array_1 = new int[8];

for (int i = 0; i < array_1.Length; i++)
{
    int number = random_num();
    array_1[i] = number;
    System.Console.WriteLine($"Элемент массива №{i + 1} = {array_1[i]}");
}

string string_array = string.Join(" ", array_1);
System.Console.WriteLine($"Весь массив справа: {string_array}");
