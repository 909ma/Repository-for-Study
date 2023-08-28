/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2839 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	scanner.close();
	if (N < 3 || N > 5000) {
	    System.out.println("ERROR N");
	    return;
	}

	int max5 = N / 5;
	int max3 = N / 3;
	System.out.println(search(max5, max3, N));

    }

    public static int search(int max5, int max3, int N) {
	int count = -1;
	for (int i = max5; i >= 0; i--) {
	    for (int j = 0; j <= max3; j++) {
		if (5 * i + 3 * j == N) {
		    count = i + j;
		    return count;
		}
	    }
	}
	return count;
    }
}
