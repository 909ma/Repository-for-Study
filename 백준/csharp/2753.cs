using System;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int year = int.Parse(Console.ReadLine());

            bool LeapYear = false;

            if (year % 4 == 0)
            {
                if (year % 100 == 0)
                {
                    if (year % 400 == 0)
                    {
                        LeapYear = true;
                    }
                    else
                    {
                        LeapYear = false;
                    }
                }
                else
                {
                    LeapYear = true;
                }
            }

            if (LeapYear)
            {
                Console.WriteLine("1");
            }
            else
            {
                Console.WriteLine("0");
            }
        }
    }
}
