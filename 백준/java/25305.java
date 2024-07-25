/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java25305 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	if (N < 1 || N > 1000) {
	    System.out.println("ERROR N");
	    scanner.close();
	    return;
	}
	int k = scanner.nextInt();
	if (k < 1 || k > N) {
	    System.out.println("ERROR k");
	    scanner.close();
	    return;
	}

	int[] list = new int[N];
	for (int i = 0; i < N; i++) {
	    list[i] = scanner.nextInt();
	    if (list[i] < 0 || list[i] > 10000) {
		System.out.println("ERROR list[" + i + "]");
		scanner.close();
		return;
	    }
	}
	scanner.close();
	Arrays.sort(list);
	System.out.println(list[N - k]);
    }
}
