using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int size = int.Parse(Console.ReadLine());
            for (int i = 1; i <= size; i++)
            {
                Console.Write(new string(' ', size - i));
                Console.WriteLine(new string('*', i));
            }
        }
    }
}
