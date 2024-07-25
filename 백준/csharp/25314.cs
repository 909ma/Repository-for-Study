using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine()) / 4;
            string answer = "";
            for (int i = 0; i < n; i++)
            {
                answer += "long ";
            }
            Console.WriteLine($"{answer}int");
        }
    }
}
