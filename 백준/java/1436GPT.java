/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1436GPT {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	scanner.close();

	int count = 0; // 666이 포함된 숫자의 개수
	int number = 0; // 숫자를 증가시키며 확인할 변수

	while (count < N) {
	    number++;

	    // 숫자에 "666"이 포함되어 있다면 count를 증가시킴
	    if (String.valueOf(number).contains("666")) {
		count++;
	    }
	}

	System.out.println(number);
    }
}
