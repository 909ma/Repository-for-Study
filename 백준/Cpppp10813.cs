using System;
using System.Collections.Generic;

namespace BAEKJOON {
    class Program {
        public static void Main(string[] args) {
            List<int> NumList = new List<int>();
            string[] inputs = Console.ReadLine().Split(' ');
            int N = int.Parse(inputs[0]);
            int M = int.Parse(inputs[1]);

            for (int i = 1; i <= N; i++){
                NumList.Add(i);
            }

            for (int i = 0; i < M; i++){
                inputs = Console.ReadLine().Split(' ');
                int a = int.Parse(inputs[0]) - 1;
                int b = int.Parse(inputs[1]) - 1;
                int temp = NumList[a];
                NumList[a] = NumList[b];
                NumList[b] = temp;
            }

            for (int i = 0; i < N; i++){
                Console.Write($"{NumList[i]} ");
            }
        }
    }
}
