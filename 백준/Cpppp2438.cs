using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int size = int.Parse(Console.ReadLine());
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j <= i; j++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();



            }
        }
    }
}

/*
int n = int.Parse(Console.ReadLine());
for(int i =1; i<=n; i++)
    Console.WriteLine(new string('*', i));

C#도 이런게 있었네
 */
