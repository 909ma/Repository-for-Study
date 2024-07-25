using System;
using System.Collections.Generic;
using System.Linq;

namespace BAEKJOON {
    class Program {
        public static void Main(string[] args) {
            int size = int.Parse(Console.ReadLine());
            string[] inputs = Console.ReadLine().Split(' ');
            
            double sum = 0;
            double max = 0;

            for (int i = 0; i < size; i++){
                double temp = double.Parse(inputs[i]);
                if (temp > max){
                    max = temp;
                }
            }
            //Console.WriteLine($"max: {max}");
            for (int i = 0; i < size; i++){
                //Console.WriteLine($"=={i}=======================");
                double temp = double.Parse(inputs[i]);
                //Console.WriteLine($"temp-before: {temp}");
                if (temp != max){
                    temp = (temp / max) * 100;
                    sum += temp;
                    //Console.WriteLine($"temp-after: {temp}");
                    //Console.WriteLine($"sum: {sum}");
                }
                else{
                    sum += 100;
                }
            }
            double answer = sum / size;
            Console.Write(answer);
        }
    }
}


/*
Max()가 왜 제대로 일을 안 하지?
*/
/*
float max = 0;
float sum = 0;

int s = int.Parse(Console.ReadLine());
string[] g = Console.ReadLine().Split();

for(int i = 0; i < s; i++)
{
    if(float.Parse(g[i]) > max)
    {
        max = float.Parse(g[i]);
    }
}

for (int i = 0; i < s; i++)
{
    sum = sum + float.Parse(g[i])/max*100;
}
Console.WriteLine(sum/(float)s);

깔끔하네
*/
