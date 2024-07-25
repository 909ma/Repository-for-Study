using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            while (true) {
                string[] inputs = Console.ReadLine().Split(' ');
                int A = int.Parse(inputs[0]);
                int B = int.Parse(inputs[1]);

                if (A == B && A == 0)
                {
                    break;
                }
                Console.WriteLine($"{A + B}");
            }
        }
    }
}
