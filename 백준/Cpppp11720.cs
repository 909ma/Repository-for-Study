using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            int num_size = int.Parse(Console.ReadLine());
            string inputs = Console.ReadLine();
            int sum = 0;
            for (int i = 0; i < num_size; i++){
                int temp = (int)inputs[i] - 48;
                sum += temp;
            }

            Console.WriteLine($"{sum}");
        }
    }
}
