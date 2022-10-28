// Задача №1

System.Console.WriteLine("Задача №1");

int size_count(int number_1)
{
    string s_number_1 = number_1.ToString();
    int size_1 = s_number_1.Length;
    System.Console.WriteLine($"Количество цифр в числе {number_1} равно: {size_1}");
    return size_1;
}

System.Console.WriteLine("Введите любое число:");
int number_1 = int.Parse(Console.ReadLine());
size_count(number_1);





// Задача №2

System.Console.WriteLine("");
System.Console.WriteLine("Задача №2");
System.Console.WriteLine("");

int multiply_sum(int number_1)
{
    int result = 1;
    for (int i = 1; i <= number_1; i++)
    {
        result = result * i;
    }
    return result;
}

Random rnd = new Random();
int number_2 = rnd.Next(1, 9);
System.Console.WriteLine($"Созданное число равно: {number_2}");
System.Console.WriteLine($"Факториалом числа {number_2} будет являться {multiply_sum(number_2)}");





// Задача №3

System.Console.WriteLine("");
System.Console.WriteLine("Задача №3");
System.Console.WriteLine("");

int number_3 = rnd.Next(0, 1);
int[] array_1 = new int[8];

int fill_array(int number_1)
{
    for (int i = 0; i < array_1.Length; i++)
    {
        array_1[i] = number_1;
        System.Console.WriteLine($"Элемент массива: {array_1[i]}");
    }
    return number_1;
}

int print_array(int[] array)
{
    int result = 1;
    for (int i = 0; i < array.Length; i++)
    {
        result = array[i];
        System.Console.WriteLine(result);
    }
    return result;
}

fill_array(number_3);
print_array(array_1);