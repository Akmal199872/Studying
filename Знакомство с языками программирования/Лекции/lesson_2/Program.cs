System.Console.WriteLine("Лекция №2");
System.Console.WriteLine("Функции");
System.Console.WriteLine("");

int max(int arg1, int arg2, int arg3) {
    int result = arg1;
    if (arg2 > result) {
        result = arg2;
    }
    if (arg3 > result) {
        result = arg3;
    }
    return result;
}

int a1 = 13;
int b1 = 14;
int c1 = 15;


int max1 = max(a1, b1, c1);

System.Console.WriteLine(max1);



System.Console.WriteLine("");
System.Console.WriteLine("Массивы");
System.Console.WriteLine("");

int [] array = {1, 2, 3, 4, 5, 61, 7, 8, 9, 61};
System.Console.WriteLine(array);

int max2 = max(max(array[0], array[1], array[2]),
                max(array[3], array[4], array[5]),
                max(array[6], array[7], array[8]));

System.Console.WriteLine(max2);


System.Console.WriteLine("");
int size = array.Length;
int find = 61;

int index = 0;
while (index < size) {
    if (array[index] == find) {
        System.Console.WriteLine(index);
        break;
    }
    index++;
}

System.Console.WriteLine("");
System.Console.WriteLine("Метод по заполнению массива случайными числами");
System.Console.WriteLine("");

void fill_array(int[] collection) {
    int length = collection.Length;
    int index = 0;
    while (index < length) {
        collection[index] = new Random().Next(1, 10);
        index++;
    }
}

void print_array(int[] col) {
    int count = col.Length;
    int position = 0;
    while (position < count) {
        System.Console.WriteLine(col[position]);
        position++;
    }
}

int indexOf(int[] collection, int find) {
    int count = collection.Length;
    int index = 0;
    int position = 0;

    while (index < count) {
        if(collection[index] == find) {
            position = index;
            break;
        }
        index++;
    }
    return position;
}

int [] array_2 = new int[10];

fill_array(array);
print_array(array);
System.Console.WriteLine("");

int pos = indexOf(array_2, 7);
System.Console.WriteLine(pos);