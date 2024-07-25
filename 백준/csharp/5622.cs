using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            string inputs = Console.ReadLine();
            int inputs_length = inputs.Length;
            int time = 0;
            for (int i = 0; i < inputs_length; i++){
                char char_temp = inputs[i];
                int int_temp = Program.DialTime(char_temp);
                time += int_temp;                
            }
            Console.Write($"{time}");
        }
        
        public static int DialTime(char temp){
            switch(temp){
            case 'A':
            case 'B':
            case 'C':
                return 3;
            case 'D':
            case 'E':
            case 'F':
                return 4;
            case 'G':
            case 'H':
            case 'I':
                return 5;
            case 'J':
            case 'K':
            case 'L':
                return 6;
            case 'M':
            case 'N':
            case 'O':
                return 7;
            case 'P':
            case 'Q':
            case 'R':
            case 'S':
                return 8;
            case 'T':
            case 'U':
            case 'V':
                return 9;
            case 'W':
            case 'X':
            case 'Y':
            case 'Z':
                return 10;
            }
            return 0;
        }
    }
}


/*
https://www.acmicpc.net/source/65110282

string str = Console.ReadLine();
string[] dial = { "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ" };

int sum = 0;
for(int i = 0; i < str.Length; i++)
{
    for(int j = 0; j < dial.Length; j++)
    {
        if (dial[j].Contains(str[i]))
        {
            sum += j + 3;
        }
    }
}
Console.WriteLine(sum);


잘했네...
*/