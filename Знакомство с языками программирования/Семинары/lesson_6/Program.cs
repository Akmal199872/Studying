// Задача №1

System.Console.WriteLine("Задача №1");
System.Console.WriteLine();

Random rnd = new Random();
int [] array = new int[3];

void PrintArray(int [] array) {
    string string_array = string.Join(" ", array);
    System.Console.WriteLine(string_array);
    
}

void FillArray(int [] array, int minValue, int maxValue) {
    for (int i = 0; i < array.Length; i++) {
        int number = rnd.Next(minValue, maxValue);
        array[i] = number;   
    }
}

void CreateTriangle(int [] array ) {
    FillArray(array, 1, 9);
    PrintArray(array);
    int max = -1;
    int index = 0;
    for (int i = 0; i < array.Length; i++) {
        if (max <= array[i]) {
            max = array[i];
            index = i;
        }
    }

    int sum = 0;

    for (int i = 0; i < array.Length; i++) {
        if (array[i] != max) {
            sum = sum + array[i];        
        }
    }
    
    System.Console.WriteLine($"Максимальная длина одной из сторон треугольника = {max}");
    System.Console.WriteLine($"Сумма двух меньших сторон треугольника = {sum}");

    if (max < sum) {
        System.Console.WriteLine("Треугольник может быть с такими параметрами");
    }
    else {
        System.Console.WriteLine("Треугольника с такими параметрами быть не может");
    }
}

CreateTriangle(array);





// Задача №2

System.Console.WriteLine();
System.Console.WriteLine("Задача №2");
System.Console.WriteLine();

System.Console.Write("Введите число для перевода в двоичное число: ");
int number = int.Parse(Console.ReadLine());
int [] array_2 = new int[number];

string TransferToBinary(int number) {
    string result = string.Empty;
    while (number > 0) {
        System.Console.WriteLine($"{result} = {result} + {number} % 2");
        result = result + number % 2;
        System.Console.WriteLine($"{number} = {number} / 2");
        number = number / 2;
    }
    System.Console.WriteLine($"Результат = {result}");
    return result;
}

TransferToBinary(number);





// Задача №3

System.Console.WriteLine("");
System.Console.WriteLine("Задача №3");
System.Console.WriteLine("");

void Fibonacci(int n) {
    int [] array = new int [n];
    FillArray(array, 1, 9);
    array[0] = 0;
    array[1] = 1;
    array[2] = 1;
    for (int i = 3; i < array.Length; i++) {
        array[i] = array[i - 1] + array[i - 2];
    }
    PrintArray(array);
}

Fibonacci(30);





// Задача №4

System.Console.WriteLine("");
System.Console.WriteLine("Задача №4");
System.Console.WriteLine("");

int [] array_3 = new int [8];
int [] array_4 = new int [8];

FillArray(array_3, 1, 9);
PrintArray(array_3);

for (int i = 0; i < array_3.Length; i++){
    int result = array_3[i];
    array_4[i] = result;
    // PrintArray(array_4);
    // array_3.CopyTo(array_4, i);
}
PrintArray(array_4.Reverse().ToArray());