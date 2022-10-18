System.Console.WriteLine("Задача №19");
System.Console.WriteLine("");

int result = 0;

while (true) {
    System.Console.Write("Ввведите число 'палиндром': ");
    int number_1 = int.Parse(Console.ReadLine());

    string s_number_1 = number_1.ToString();
    int size_1 = s_number_1.Length;
    int count_1 = 1;

    if (s_number_1[count_1 - 1] == s_number_1[size_1 - 1]) {
        count_1++;
        result = number_1;
        break;
    }
    else {
        System.Console.WriteLine("Число не является палиндромом. Введите число заново.");
    }
}
System.Console.WriteLine($"Число, которое является палиндромом равно: {result}");