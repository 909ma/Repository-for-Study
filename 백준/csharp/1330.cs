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

            if (a > b)
            {
                Console.WriteLine(">");
            }
            else if (b > a)
            {
                Console.WriteLine("<");
            }
            else
            {
                Console.WriteLine("==");
            }
        }
    }
}
