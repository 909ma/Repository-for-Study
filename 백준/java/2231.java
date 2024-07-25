/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2231 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	scanner.close();
	if (N < 1 || N > 1000000) {
	    System.out.println("ERROR N");
	    return;
	}
	int M = 0;

	for (int i = 1; i <= N; i++) {
	    int sum = i + i % 10 + i / 10 % 10 + i / 100 % 10 + i / 1000 % 10 + i / 10000 % 10 + i / 100000 % 10
		    + i / 1000000 % 10;
	    if (sum == N) {
		M = i;
		break;
	    }
	}

	System.out.println(M);
    }
}
