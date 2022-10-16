// Задача №2

Console.WriteLine("Задача №2");
Console.WriteLine("");

Console.WriteLine("Введите первое число");
int a = int.Parse(Console.ReadLine());
Console.WriteLine("Введите второе число");
int b = int.Parse(Console.ReadLine());

int max = 0;
int min = 0;

if (a > b) {
    max = a;
    min = b;
    System.Console.WriteLine("Большее число = " + max);
    System.Console.WriteLine("Меньшее число = " + min);
}
else {
    max = b;
    min = a;
    System.Console.WriteLine("Большее число = " + max);
    System.Console.WriteLine("Меньшее число = " + min);
}


// Задача №4

System.Console.WriteLine("");
System.Console.WriteLine("Задача №4");
System.Console.WriteLine();

System.Console.WriteLine("Введите первое число");
int c = int.Parse(Console.ReadLine());
System.Console.WriteLine("Введите второе число");
int d = int.Parse(Console.ReadLine());
System.Console.WriteLine("Введите третье число");
int e = int.Parse(Console.ReadLine());

int max_1 = 0;
if (c > d) {
    if (c > e) {
        max_1 = c;
        System.Console.WriteLine("Максимальное число = " + max_1);
    }
    else {
        max_1 = e;
        System.Console.WriteLine("Максимальное число = " + max_1);
    }
}
else {
    if (d > e) {
        max_1 = d;
        System.Console.WriteLine("Максимальное число = " + max_1);
    }
    else {
        max_1 = e;
        System.Console.WriteLine("Максимальное число = " + max_1);
    }
}


// Задача №6

System.Console.WriteLine("");
System.Console.WriteLine("Задача №6");
System.Console.WriteLine("");

System.Console.WriteLine("Введите любое число");
int f = int.Parse(Console.ReadLine());

if (f % 2 == 0) {
    System.Console.WriteLine("Делится без остатка");
}
else {
    System.Console.WriteLine("Делится с остатком");
}


// Задача №8

System.Console.WriteLine("");
System.Console.WriteLine("Задача №8");
System.Console.WriteLine("");

System.Console.WriteLine("Введите любое число");
int N = int.Parse(Console.ReadLine());
int i = 1;

System.Console.WriteLine("");
System.Console.WriteLine("Цикл запущен");

while (i <= N) {
    if (i % 2 == 0) {
        System.Console.WriteLine(i);
    }
    i++;
}
