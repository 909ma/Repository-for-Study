using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            int N = int.Parse(inputs[0]);
            int X = int.Parse(inputs[1]);
            inputs = Console.ReadLine().Split(' ');
            for (int i = 0; i < N; i++)
            {
                int temp = int.Parse(inputs[i]);
                if (temp < X)
                {
                    Console.Write($"{temp} ");
                }
            }
        }
    }
}
