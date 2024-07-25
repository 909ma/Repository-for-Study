using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int size = int.Parse(Console.ReadLine());
            string[] inputs = Console.ReadLine().Split(' ');
            int search = int.Parse(Console.ReadLine());
            int answer = 0;
            for (int i = 0; i < size; i++)
            {
                if (int.Parse(inputs[i]) == search)
                {
                    answer++;
                }
            }

            Console.WriteLine(answer);
        }
    }
}
