// Задача №1

System.Console.WriteLine("Задача №1");
System.Console.WriteLine("");
string[,] table = new string [2,5];
table[1, 2] = "слово";

for (int rows = 0; rows < 2; rows++) {
    for (int columns = 0; columns < 5; columns++) {
        System.Console.WriteLine($"-{table[rows,columns]}-");
    }
}



// Задача №2

System.Console.WriteLine("");
System.Console.WriteLine("Задача №2");
System.Console.WriteLine("");

void PrintArray(int [,] matr) {
    for (int rows = 0; rows < matr.GetLength(0); rows++) {
        for (int columns = 0; columns < matr.GetLength(1); columns++) {
            System.Console.Write($"{matr[rows,columns]} ");
        }
        System.Console.WriteLine();
    }
}

void FillArray(int [,] matr) {
    for (int i = 0; i < matr.GetLength(0); i++) {
        for (int j = 0; j < matr.GetLength(1); j++) {
            matr[i, j] = new Random().Next(1, 10);
        }
    }
}


int [,] matrix = new int [3, 4];

PrintArray(matrix);
FillArray(matrix);
System.Console.WriteLine("");
PrintArray(matrix);



// Задача №3

System.Console.WriteLine("");
System.Console.WriteLine("Задача №3");
System.Console.WriteLine("");

int [,] pic = new int[,] {
    {0,0,0,0},
    {0,1,0,0},
    {1,1,0,0},
    {0,1,1,0}
};

void PrintImage(int [,] image) {
    for (int rows = 0; rows < image.GetLength(0); rows++) {
        for (int columns = 0; columns < image.GetLength(1); columns++) {
            // System.Console.Write($"{image[rows,columns]} ");
            if (image[rows,columns] == 0) {
                System.Console.Write($" ");
            }
            else {
                System.Console.Write($"+");
            }
        }
        System.Console.WriteLine();
    }
}

void FillImage(int row, int col) {
    if (pic[row,col] == 0) {
        pic[row,col] = 1;
        FillImage(row - 1, col);
        FillImage(row, col - 1);
        FillImage(row + 1, col);
        FillImage(row, col + 1);
    }
}


PrintImage(pic);
FillImage(1, 1);
PrintImage(pic);



// Задача №4

System.Console.WriteLine("");
System.Console.WriteLine("Задача №4");
System.Console.WriteLine("");

double Factorial(int n) {
    if (n == 1) {
        return 1;
    }
    else {
        return n * Factorial(n - 1);
    }
}
for (int i = 1; i < 40; i++) {
    System.Console.WriteLine($"{i}! = {Factorial(i)}");    
}



// Задача №5

System.Console.WriteLine("");
System.Console.WriteLine("Задача №5");
System.Console.WriteLine("");

double Fibonacci(int n) {
    if (n == 1 || n == 2) {
        return 1;
    }
    else {
        return Fibonacci(n-1) + Fibonacci(n-2);
    }
}

for (int i = 1; i < 50; i++) {
    System.Console.WriteLine($"f({i}) = {Fibonacci(i)}");
}



// Задача №6

System.Console.WriteLine("");
System.Console.WriteLine("Задача №6");
System.Console.WriteLine("");

