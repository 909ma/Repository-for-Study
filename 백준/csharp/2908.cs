using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            string[] inputs = Console.ReadLine().Split(' ');
            int num_a = int.Parse(inputs[0]);
            int num_b = int.Parse(inputs[1]);
            num_a = Program.Reverse(num_a);
            num_b = Program.Reverse(num_b);
            Console.Write($"{Math.Max(num_a, num_b)}");
        }

        public static int Reverse(int num) {
            int num_temp = 0;
            while (num != 0) {
                num_temp *= 10;
                num_temp += num % 10;
                num /= 10;
            }
            return num_temp;
        }
    }
}
