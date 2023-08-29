using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split(' ');

            decimal A = decimal.Parse(input[0]);
            decimal B = decimal.Parse(input[1]);
            decimal C = decimal.Parse(input[2]);

            decimal answer = A + B + C;

            Console.WriteLine(answer);
        }
    }
}
