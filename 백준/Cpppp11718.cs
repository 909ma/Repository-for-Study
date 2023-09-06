using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            int inputChar;

            while ((inputChar = Console.Read()) != -1) {
                char character = (char)inputChar;
                Console.Write(character);
            }
        }
    }
}

/*
https://www.acmicpc.net/source/63154448

Console.Write(Console.In.ReadToEnd());

이건 처음보네;
Console.Write(Console.In.ReadToEnd());: 이 코드는 Console.In을 사용하여 콘솔에서 입력을 읽어와서 Console.Write를 사용하여 그대로 출력합니다. ReadToEnd() 메서드는 입력 스트림에서 끝까지 모든 내용을 읽어옵니다.
*/