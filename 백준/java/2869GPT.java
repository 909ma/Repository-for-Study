/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2869GPT {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);

	int A = scanner.nextInt(); // 낮에 올라가는 높이
	int B = scanner.nextInt(); // 밤에 미끄러지는 높이
	int V = scanner.nextInt(); // 나무 막대의 높이

	int day = (V - B) / (A - B);
	if ((V - B) % (A - B) != 0) {
	    day++;
	}

	System.out.println(day);

	scanner.close();
    }
}
