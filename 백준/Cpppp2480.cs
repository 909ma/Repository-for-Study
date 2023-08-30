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

            int money = 0;

            if (a == b && a == c)
            {
                money += 10000 + a * 1000;
            }
            else if ((a == b) || (a == c))
            {
                money += 1000 + a * 100;
            }
            else if (b == c)
            {
                money += 1000 + b * 100;
            }
            else
            {
                if ((a > b) && (a > c))
                {
                    money += a * 100;
                }
                else if ((b > a) && (b > c))
                {
                    money += b * 100;
                }
                else
                {
                    money += c * 100;
                }
            }

            Console.WriteLine(money);
        }
    }
}

// 그냥 Array.Sort(i); 쓸껄...