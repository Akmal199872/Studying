var number = 12;
System.Console.WriteLine(number.GetType().Name);

var data = new int[] { 1, 2, 3, 4 }
        .Where(e => e > 0)
        .Select(e => new { q = e, w = e + 1 });

System.Console.WriteLine(data.GetType().Name);
