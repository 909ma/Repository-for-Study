using System;
using System.Collections.Generic;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            int N = int.Parse(inputs[0]);
            int M = int.Parse(inputs[1]);
            List<int> bowl = new List<int>();

            for (int i = 0; i < N; i++)
            {
                bowl.Add(0);
            }

            for (int i = 0; i < M; i++)
            {
                inputs = Console.ReadLine().Split(' ');
                int a = int.Parse(inputs[0]) - 1;
                int b = int.Parse(inputs[1]);
                int c = int.Parse(inputs[2]);

                for (int j = a; j < b; j++)
                {
                    bowl[j] = c;
                }
            }

            for (int i = 0; i < N; i++)
            {
                Console.Write($"{bowl[i]} ");
            }
        }
    }
}
