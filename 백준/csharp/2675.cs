using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            int test_case = int.Parse(Console.ReadLine());
            for (int i = 0; i < test_case; i++) {
                string[] inputs = Console.ReadLine().Split(' ');
                int loop_num = int.Parse(inputs[0]);
                string input_text = inputs[1];
                int text_length = input_text.Length;

                for (int j = 0; j < text_length; j++) {
                    for (int k = 0; k < loop_num; k++) {
                        Console.Write(input_text[j]);
                    
                }}
                Console.Write("\n");
            }
        }
    }
}
