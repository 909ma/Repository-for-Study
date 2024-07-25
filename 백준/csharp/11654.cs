using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            char input = Console.ReadLine()[0];
            int asciiValue = (int)input;
            Console.WriteLine(asciiValue);
        }
    }
}
