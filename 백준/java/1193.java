/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 분수찾기 https://www.acmicpc.net/problem/1193
문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.

예제 입력 1 
1
예제 출력 1 
1/1
예제 입력 2 
2
예제 출력 2 
1/2
예제 입력 3 
3
예제 출력 3 
2/1
예제 입력 4 
4
예제 출력 4 
3/1
예제 입력 5 
5
예제 출력 5 
2/2
예제 입력 6 
6
예제 출력 6 
1/3
예제 입력 7 
7
예제 출력 7 
1/4
예제 입력 8 
8
예제 출력 8 
2/3
예제 입력 9 
9
예제 출력 9 
3/2
예제 입력 10 
14
예제 출력 10 
2/4
 */
package practice;

import java.util.Scanner;

public class Java1193 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int order = scanner.nextInt();
	scanner.close();
	if (order < 1 || order > 10000000) {
	    System.out.println("ERROR");
	    return;
	}
	int start = 1;
	int end = 1;
	int count = 1;

	for (int i = 1;; i++) {
	    if (order >= start && order <= end) {
		break;
	    }
	    start = end + 1;
	    end = start + i;
	    count++;
	}
	// System.out.printf("count : %d, start : %d, end : %d\n", count, start, end);
	if (count % 2 == 0) {

	    System.out.printf("%d/%d\n", 1 + (order - start), count - (order - start));
	} else {

	    System.out.printf("%d/%d\n", count - (order - start), 1 + (order - start));
	}
    }
}
