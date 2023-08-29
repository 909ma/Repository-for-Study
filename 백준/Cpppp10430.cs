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
            int c = int.Parse(inputs[2]);
            int answer1 = (a + b) % c;
            int answer2 = ((a % c) + (b % c)) % c;
            int answer3 = (a * b) % c;
            int answer4 = ((a % c) * (b % c)) % c;
            Console.WriteLine($"{answer1}\n{answer2}\n{answer3}\n{answer4}");
        }
    }
}
