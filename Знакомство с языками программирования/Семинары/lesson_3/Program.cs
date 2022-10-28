// Задача №1

System.Console.WriteLine("Введите четверть для определения координат");
int number = int.Parse(Console.ReadLine());
int[,] array = new int[4, 2];

array[0, 0] = 1;
array[0, 1] = 1;

array[1, 0] = -1;
array[1, 1] = 1;

array[2, 0] = -1;
array[2, 1] = -1;

array[3, 0] = 1;
array[3, 1] = -1;

int x = 0;
int y = 0;

int minx = array[number - 1, 0];
int miny = array[number - 1, 1];
string maxy = "";
string maxx = "";
if (minx > 0)
{
    maxx = "infinity";
}
else
{
    maxx = "-infinity";
}
if (miny > 0)
{
    maxy = "infinity";
}
else
{
    maxy = "-infinity";
}
System.Console.WriteLine($"from x = {minx} to x = {maxx}");
System.Console.WriteLine($"from y = {miny} to y = {maxy}");




// Задача №2


int[,] array_1 = new int[2, 2];

array_1[0, 0] = 3;
array_1[0, 1] = 6;
array_1[1, 0] = 2;
array_1[1, 1] = 1;


Корень от((x1-x2)^2 + (y1 - y2) ^ 2)

double result_1 = Math.Pow(array_1[0, 0] - array_1[1, 0], 2) + Math.Pow(array_1[0, 1] - array_1[1, 1], 2);
double result_2 = Math.Sqrt(result_1);

System.Console.WriteLine(result_2);





// Задача №3

int number_1 = int.Parse(Console.ReadLine());

int[] array = new int[number_1];
for (int i = 1; i <= number_1; i++)
{
    System.Console.WriteLine(Math.Pow(i, 2));
}

