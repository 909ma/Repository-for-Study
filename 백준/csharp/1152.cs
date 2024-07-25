using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            string[] inputs = Console.ReadLine().Trim().Split(' ');
            int inputs_length = inputs.Length;
            // 공백 하나만 들어오는 경우 예외처리
            if (inputs_length == 1){
                if (inputs[0] == ""){
                    inputs_length = 0;
                }
            }
            Console.Write(inputs_length);
        }
    }
}



/* 
C#은 Strip()은 없고 Trim()을 써야 하구나
공백 하나 들어오는 경우도 생각해야했네
*/

/*
Console.Write(Console.ReadLine().Split().Count(s=>s!=""));

한 줄로도 적을 수 있었네
*/