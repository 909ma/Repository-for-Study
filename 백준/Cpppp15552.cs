using System;
using System.IO;

namespace BAEKJOON
{
    internal class Program
    {
        static void Main(string[] args)
        {
            StreamReader reader = new StreamReader(Console.OpenStandardInput());
            StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

            int testCaseCount = int.Parse(reader.ReadLine());

            for (int i = 0; i < testCaseCount; i++)
            {
                string[] input = reader.ReadLine().Split();
                int a = int.Parse(input[0]);
                int b = int.Parse(input[1]);

                writer.WriteLine(a + b);
            }

            writer.Flush();
            writer.Close();
        }
    }
}
