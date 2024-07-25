using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int input1 = int.Parse(Console.ReadLine());
            int input2 = int.Parse(Console.ReadLine());

            int answer3 = input1 * (input2 % 10);
            int answer4 = input1 * ((input2 / 10) % 10);
            int answer5 = input1 * ((input2 / 100) % 10);
            int answer6 = input1 * input2;

            Console.WriteLine($"{answer3}\n{answer4}\n{answer5}\n{answer6}");
        }
    }
}
