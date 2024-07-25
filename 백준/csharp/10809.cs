using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            int[] num_list = new int[26];
            
            for (int i = 0; i < num_list.Length; i++) {
                num_list[i] = -1;
            }

            string inputs = Console.ReadLine();
            int inputs_length = inputs.Length;
                
            for (int i = 0; i < inputs_length; i++){
                char temp_char = inputs[i];
                int temp_char_num = (int)temp_char - 97;
                if (num_list[temp_char_num] == -1){
                    num_list[temp_char_num] = i;
                }
            }

            for (int i = 0; i < num_list.Length; i++) {
                Console.Write($"{num_list[i]} ");
            }
        }
    }
}
