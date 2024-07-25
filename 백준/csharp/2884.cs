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

            M -= 45;

            if (M < 0)
            {
                M += 60;
                H--;

                if (H < 0)
                {
                    H += 24;
                }
            }

            Console.WriteLine($"{H} {M}");
        }
    }
}
