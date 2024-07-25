using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int size = int.Parse(Console.ReadLine());

            for (int i = 1; i <= size; i++)
            {
                string[] inputs = Console.ReadLine().Split(' ');
                int a = int.Parse(inputs[0]);
                int b = int.Parse(inputs[1]);
                Console.WriteLine(a + b);
            }
        }
    }
}
