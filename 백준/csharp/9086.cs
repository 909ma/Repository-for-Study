using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            int test_case = int.Parse(Console.ReadLine());
            for (int i = 0; i < test_case; i++){
                string inputs = Console.ReadLine();
                int num = inputs.Length;
                Console.WriteLine($"{inputs[0]}{inputs[num-1]}");
            }
        }
    }
}