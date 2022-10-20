// Задача №25

System.Console.WriteLine("Задача №25");
System.Console.WriteLine("");

System.Console.Write("Введите первое число: ");
int number_1 = int.Parse(Console.ReadLine());
System.Console.Write("Введите второе число: ");
int number_2 = int.Parse(Console.ReadLine());

int result = 1;

for (int i = 1; i < number_2; i++) {
    for (int j = 0; j < number_2; j++) {
        result = result * number_1;
    }
}

System.Console.WriteLine($"Результатом возведения в степень {result}");




