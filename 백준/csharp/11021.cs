using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int size = int.Parse(Console.ReadLine());
            for (int i = 0; i < size; i++)
            {
                string[] inputs = Console.ReadLine().Split(' ');
                int A = int.Parse(inputs[0]);
                int B = int.Parse(inputs[1]);

                Console.WriteLine($"Case #{i + 1}: {A + B}");
            }
        }
    }
}
