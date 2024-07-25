/*
 * @Author : 909ma
 * 
 * @Date : 2023. 5. 21
 * 
 * @Function : 이거 왜 정답이 아니라고 나오지? 분석해야됨
 */

package practice;

import java.util.Scanner;

public class Java2675 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);

	int testCase = Integer.parseInt(scanner.nextLine());
	if (testCase < 1 || testCase > 1000) {
	    System.out.println("ERROR");
	    scanner.close();
	    return;
	}

	int[] repeate = new int[testCase];
	String[] inputString = new String[testCase];
	for (int i = 0; i < testCase; i++) {
	    repeate[i] = Integer.parseInt(scanner.nextLine());
	    if (repeate[i] < 1 || repeate[i] > 8) {
		System.out.println("ERROR");
		scanner.close();
		return;
	    }
	    inputString[i] = scanner.nextLine();
	    if (inputString[i].length() > 20 || inputString[i].length() < 1) {
		System.out.println("ERROR");
		scanner.close();
		return;
	    }
	}
	scanner.close();

	// 실질적 알고리즘
	for (int i = 0; i < testCase; i++) {
	    for (int j = 0; j < inputString[i].length(); j++) {
		for (int k = 0; k < repeate[i]; k++) {
		    System.out.print(inputString[i].charAt(j));
		}
	    }
	    System.out.println(); // 개행 문자 추가
	}
    }
}
