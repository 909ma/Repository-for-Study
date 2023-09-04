using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int index = 0;
            int max = 0;
            for (int i = 1; i <= 9; i++)
            {
                if (i == 1)
                {
                    index = 1;
                    max = int.Parse(Console.ReadLine());
                }
                else
                {
                    int temp = int.Parse(Console.ReadLine());
                    if (temp > max)
                    {
                        max = temp;
                        index = i;
                    }
                }
            }
            Console.WriteLine($"{max}\n{index}");
        }
    }
}
