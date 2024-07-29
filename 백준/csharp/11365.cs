using System;

namespace BAEKJOON {
    class Program {
        public static void Main(string[] args) {
            string message;
            while(true){
                message = Console.ReadLine();

                if (message == "END"){
                    break;
                }

                char[] charArray = message.ToCharArray();
                Array.Reverse(charArray);
                Console.WriteLine(new string(charArray));
            }
        }
    }
}
