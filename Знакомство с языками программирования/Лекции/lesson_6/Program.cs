// Задача №1
using System.Linq;

string EmptyString()
{
    return string.Empty;
}

System.Console.WriteLine("Задача №1");
EmptyString();



string text = "(1,2) (2,3) (4,5) (6,7)"

        .Replace("(", "")
        .Replace(")", "");

System.Console.WriteLine(text);
var data = text.Split(" ")
        .Select(item => item.Split(','))
        .Select(e => (x: int.Parse(e[0]), y: int.Parse(e[1])))
        .Where(e => e.x % 2 == 0)
        .Select(point => (point.x * 10, point.y))
        .ToArray();


for (int i = 0; i < data.Length; i++)
{
    System.Console.WriteLine(data[i]);
    EmptyString();
}