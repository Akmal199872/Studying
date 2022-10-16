// int num = new Random().Next(1, 10);
// Console.Write(num);

// double numA = 6;
// double numB = 2.5;
// Console.WriteLine(numB/numA);

// Console.WriteLine("Введите имя пользователя: ");
// string username = Console.ReadLine();

// if (username.ToLower() == "Маша") {
//     Console.WriteLine("Ура, это же Маша!");
// }
// else {
//     Console.WriteLine("Привет, " + username);
// }

// Console.SetCursorPosition(10, 4);
// Console.WriteLine("+");
Console.Clear();
int xa = 1, ya = 1, xb = 1, yb = 30, xc = 80, yc = 30;

// Console.SetCursorPosition(xa, ya);
// Console.WriteLine("+");

// Console.SetCursorPosition(xb, yb);
// Console.WriteLine("+");

// Console.SetCursorPosition(xc, yc);
// Console.WriteLine("+");

int x = xa;
int y = xb;
int count = 0;

while(count < 10) {
    int what = new Random().Next(0, 3);
    if (what == 0) {
        x = (x + xa) / 2;
        y = (y + ya) / 2;
    }
    if (what == 1) {
        x = (x + xb) / 2;
        y = (y + yb) / 2;
    }
    if (what == 2) {
        x = (x + xc) / 2;
        y = (y + yc) / 2;
    }

    Console.SetCursorPosition(x, y);
    Console.WriteLine("+");
    count++;
}