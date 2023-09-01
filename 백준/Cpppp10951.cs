using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string inputs;
            while ((inputs = Console.ReadLine()) != null) {
                string[] inputs2 = inputs.Split(' ');
                int A = int.Parse(inputs2[0]);
                int B = int.Parse(inputs2[1]);
                Console.WriteLine($"{A + B}");
            }
        }
    }
}
