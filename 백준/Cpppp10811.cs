using System;
using System.Collections.Generic;
using System.Linq;

namespace BAEKJOON {
    class Program {
        public static void Main(string[] args) {
            List<int> NumList = new List<int>();
            List<int> TempList = new List<int>();
            string[] inputs = Console.ReadLine().Split(' ');
            
            int N = int.Parse(inputs[0]);
            int M = int.Parse(inputs[1]);
            
            for (int i= 1; i <= N; i++){
                NumList.Add(i);
            }
            
            for (int i = 0; i < M; i++){
                inputs = Console.ReadLine().Split(' ');
                int a = int.Parse(inputs[0]);
                int b = int.Parse(inputs[1]);

                for (int j = a - 1; j < b; j++){
                    TempList.Add(NumList[j]);
                }
                TempList.Reverse();
                for (int j = a - 1; j < b; j++){
                    NumList[j] = TempList[j - a + 1];
                }

                TempList.Clear();
            }

            for (int i = 0; i < N; i++){
                Console.Write($"{NumList[i]} ");
            }
        }
    }
}


/*
int[] n = Array.ConvertAll(Console.ReadLine().Split(),int.Parse);
int[] arr = Enumerable.Range(0, n[0]+1).ToArray();
while (n[1]-- > 0)
{
    int[] m = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    Array.Reverse(arr, m[0], m[1] - m[0] + 1);
}
Console.WriteLine(string.Join(" ", arr[1..(n[0]+1)]));


Reverse()가 있었네...
int[] arr = Enumerable.Range(0, n[0]+1).ToArray(); 이거는 잘 써먹자
*/
