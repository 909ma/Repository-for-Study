/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2581 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int M = scanner.nextInt();
	if (M < 1 || M > 10000) {
	    System.out.println("ERROR M");
	    scanner.close();
	    return;
	}
	int N = scanner.nextInt();
	if (N < M || N > 10000) {
	    System.out.println("ERROR N");
	    scanner.close();
	    return;
	}
	scanner.close();

	int sum = 0;
	int min = N;
	for (int i = M; i <= N; i++) {
	    int count = 0;
	    for (int j = 1; j <= i; j++) {
		if (i % j == 0) {
		    count++;
		}
		if (count > 2) {
		    break;
		}
	    }
	    if (count == 2) {
		sum += i;
		if (min > i) {
		    min = i;
		}
	    }
	}
	if (sum != 0) {
	    System.out.println(sum);
	    System.out.println(min);
	} else {
	    System.out.println(-1);
	}
    }
}
