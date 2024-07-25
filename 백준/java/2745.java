/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 진법 변환 https://www.acmicpc.net/problem/2745
문제
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

출력
첫째 줄에 B진법 수 N을 10진법으로 출력한다.

예제 입력 1 
ZZZZZ 36
예제 출력 1 
60466175
 */
package practice;

import java.util.Scanner;

public class Java2745 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);

	String[] line = scanner.nextLine().split(" ");
	String number = line[0];
	int base = Integer.parseInt(line[1]);

	if (base < 2 || base > 36) {
	    System.out.println("ERROR base");
	    scanner.close();
	    return;
	}
	scanner.close();
	// A:65, Z:90
	// 0:48, 0:57
	int numberBase10 = 0;
	int baseCount = 1;
	int length = number.length();
	for (int i = 0; i < length; i++) {
	    char c = number.charAt(length - (i + 1));
	    if (c >= '0' && c <= '9') {
		numberBase10 += baseCount * ((int) c - '0');
	    } else if (c >= 'A' && c <= 'Z') {
		numberBase10 += baseCount * ((int) c - 'A' + 10);
	    } else {
		System.out.println("ERROR number");
		return;
	    }
	    baseCount *= base;
	}

	System.out.println(numberBase10);
    }
}
