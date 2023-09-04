using System;
using System.Collections.Generic;
using System.Linq;

namespace BAEKJOON {
    class Program {
        public static void Main(string[] args) {
            List<int> NumList = new List<int>();
            for (int i = 0; i < 10; i++){
                int temp = int.Parse(Console.ReadLine());
                temp %= 42;
                NumList.Add(temp);
            }
            NumList = NumList.Distinct().ToList();
            Console.Write($"{NumList.Count}");
        }
    }
}


/*
int[] arr = new int[10];
for (int i = 0; i < 10; ++i)
arr[i] = int.Parse(Console.ReadLine()) % 42;
Console.Write(arr.Distinct().Count());

이렇게도 할 수 있네
*/
