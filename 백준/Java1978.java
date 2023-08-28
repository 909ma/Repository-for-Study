/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 소수 찾기 https://www.acmicpc.net/problem/1978
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1 
4
1 3 5 7
예제 출력 1 
3
 */
package practice;

import java.util.Scanner;

public class Java1978 {
    public static void main(String[] args) {
	boolean errorChecker = false; // 오류검사기
	Scanner scanner = new Scanner(System.in);
	int testCase = scanner.nextInt();
	// 예외처리
	if (testCase < 1 || testCase > 100) {
	    System.out.println("ERROR testCase");
	    errorChecker = true;
	}
	int[] number = new int[testCase];
	for (int i = 0; i < testCase; i++) {
	    number[i] = scanner.nextInt();
	    // 예외처리
	    if (number[i] < 1 || number[i] > 1000) {
		System.out.println("ERROR number[" + i + "]");
		errorChecker = true;
	    }
	}
	scanner.close();

	// 예외처리
	if (errorChecker) {
	    return;
	}

	int count = 0;
	for (int i = 0; i < testCase; i++) {
	    int factorCount = 0;
	    for (int j = 1; j <= number[i]; j++) {
		if (number[i] % j == 0) {
		    factorCount++;
		}
	    }
	    if (factorCount == 2) {
		count++;
	    }
	}

	System.out.println(count);
    }
}
