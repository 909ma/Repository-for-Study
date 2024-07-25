using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            int a = int.Parse(inputs[0]);
            int b = int.Parse(inputs[1]);

            int result1 = a + b;
            int result2 = a - b;
            int result3 = a * b;
            int result4 = a / b;
            int result5 = a % b;

            Console.WriteLine($"{result1}\n{result2}\n{result3}\n{result4}\n{result5}");
        }
    }
}
