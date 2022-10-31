void IntroTask(int number)
{
    System.Console.WriteLine($"{string.Empty}\nЗадача №{number}\n{string.Empty}");
}

// Задача №1

IntroTask(1);

string NumbersRec(int a, int b)
{
    if (a <= b) return $"{a} " + NumbersRec(a + 1, b);
    else return string.Empty;
}

System.Console.WriteLine(NumbersRec(1, 10));

// Задача №2

IntroTask(2);

int SumRec(int n)
{
    if (n == 0) return 0;
    else return n + SumRec(n - 1);
}

System.Console.WriteLine(SumRec(5));

// Задача №3

IntroTask(3);

int Factorial(int n)
{
    if (n == 1) return 1;
    else return n * Factorial(n-1);
}

System.Console.WriteLine(Factorial(5));

// Задача №4

IntroTask(4);

int Power(int a, int n)
{
    if (n==0) return 1;
    else return Power(a, n - 1) * a;
}

System.Console.WriteLine(Power(4, 3));

// Задача №5

IntroTask(5);

int CountLetters(string input_word, int start_letter_num)
{
    if (start_letter_num >= input_word.Length) return 0;
    else
    {
        System.Console.WriteLine($"{start_letter_num + 1} буква = [{input_word[start_letter_num]}]");
        if (start_letter_num > 0 && input_word[start_letter_num] == ' ' && input_word[start_letter_num - 1] != ' ') 
        {
            return 1 + CountLetters(input_word, start_letter_num + 1);
        }
        else return CountLetters(input_word, start_letter_num + 1);
    }
}

CountLetters("Привет, как дела?", 0);

// Задача №6

IntroTask(6);

int n = 0;
void FindWords(string alphabet, char [] word, int length = 0)
{
    if (length == word.Length)
    {
        System.Console.WriteLine($"{n++} {new String(word)}");
        return;
    }
    for (int i = 0; i < alphabet.Length; i++)
    {
        word[i] = alphabet[i];
        FindWords(alphabet, word, length + 1);
    }
}

FindWords("аисв", new char[5]);

string path = "C:/Users/akmal/Desktop/Новая папка/Studying/Знакомство с языками программирования/Домашнее задание/homework_8";
DirectoryInfo dir = new DirectoryInfo(path);
System.Console.WriteLine(dir.CreationTime);

FileInfo [] fi = dir.GetFiles();
for (int i = 0; i < fi.Length; i++)
{
    System.Console.WriteLine(fi[i].Name);
}

// Задача №7

IntroTask(7);

void CatalogInfo(string path, string indent = "")
{
    DirectoryInfo catalog = new DirectoryInfo(path);
    DirectoryInfo[] catalogs = catalog.GetDirectories();
    for (int i = 0; i < catalogs.Length; i++)
    {
        System.Console.WriteLine($"{indent}{catalogs[i].Name}");
        CatalogInfo(catalogs[i].FullName, indent + " ");
    }
    FileInfo[] files = catalog.GetFiles();
}

CatalogInfo(path);

// Задача №8

IntroTask(8);

void Towers(string with = "1", string on = "3", string some = "2", int count = 3)
{
    if (count > 1) Towers(with, some, on, count - 1);
    System.Console.WriteLine($"{with} >> {on}");
    if (count > 1) Towers(some, on, with, count -1);
}

Towers();

// Задача №9

IntroTask(9);

string [] tree = {string.Empty, "/", "*", "10", "-", "+", string.Empty, string.Empty, "4", "2", "1", "3"};
void InOrderTraversal(int pos = 1)
{
    if (pos < tree.Length)
    {
        int left = 2 * pos;
        int right = 2 * pos + 1;
        if (left < tree.Length && !String.IsNullOrEmpty(tree[left])) InOrderTraversal(left);
        System.Console.WriteLine(tree[pos]);
        if (right < tree.Length && !String.IsNullOrEmpty(tree[right])) InOrderTraversal(right);
    }
}

