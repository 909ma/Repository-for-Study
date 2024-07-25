using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            int H = int.Parse(inputs[0]);
            int M = int.Parse(inputs[1]);

            int time = int.Parse(Console.ReadLine());

            M += time;

            if (M >= 60)
            {
                H += (M / 60);
                M = M % 60;

                if (H >= 24)
                {
                    H %= 24;
                }
            }

            Console.WriteLine($"{H} {M}");
        }
    }
}
