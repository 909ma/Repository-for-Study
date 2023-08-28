/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 진법 변환 2 https://www.acmicpc.net/problem/11005
문제
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

출력
첫째 줄에 10진법 수 N을 B진법으로 출력한다.

예제 입력 1 
60466175 36
예제 출력 1 
ZZZZZ
 */
package practice;

import java.util.Scanner;

public class Java11005 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int numberBase10 = scanner.nextInt();
	int baseNumber = scanner.nextInt();
	scanner.close();

	if (numberBase10 < 1 || numberBase10 > 1000000000) {
	    System.out.println("ERROR numberBase10");
	    return;
	}
	if (baseNumber < 2 || baseNumber > 36) {
	    System.out.println("ERROR baseNumber");
	    return;
	}

	StringBuilder sb = new StringBuilder();
	while (numberBase10 > 0) {
	    int remain = numberBase10 % baseNumber;
	    char c;
	    if (remain < 10) {
		c = (char) (remain + '0');
	    } else {
		c = (char) (remain - 10 + 'A');
	    }
	    sb.insert(0, c);
	    numberBase10 /= baseNumber;
	}

	System.out.println(sb);
    }

}
