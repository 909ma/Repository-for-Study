using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int size = int.Parse(Console.ReadLine());
            string[] inputs = Console.ReadLine().Split(' ');
            int min = int.Parse(inputs[0]);
            int max = int.Parse(inputs[0]);

            for (int i = 0; i < size; i++)
            {
                int temp = int.Parse(inputs[i]);
                if (temp < min) { min = temp; }
                if (temp > max) { max = temp; }
            }

            Console.WriteLine($"{min} {max}");
        }
    }
}
