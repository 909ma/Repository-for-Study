using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            string inputs = Console.ReadLine();
            int num = int.Parse(Console.ReadLine());
            Console.WriteLine(inputs[num-1]);
        }
    }
}