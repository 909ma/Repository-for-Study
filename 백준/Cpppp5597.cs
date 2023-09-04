using System;
using System.Collections.Generic;

namespace BAEKJOON {
    class Program {
        public static void Main(string[] args) {
            List<int> NumList = new List<int> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30};
            for (int i = 0; i < 28; i++){
                int InputNum = int.Parse(Console.ReadLine());
                NumList.Remove(InputNum);
            }
            NumList.Sort();
            Console.Write($"{NumList[0]}\n{NumList[1]}");
        }
    }
}
