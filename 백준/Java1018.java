/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1018 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	int M = scanner.nextInt();
	if (N < 8 || N > 50) {
	    System.out.println("ERROR N");
	    scanner.close();
	    return;
	}
	if (M < 8 || M > 50) {
	    System.out.println("ERROR M");
	    scanner.close();
	    return;
	}
	scanner.nextLine();
	String[] board = new String[N];
	for (int i = 0; i < N; i++) {
	    board[i] = scanner.nextLine();
	}
	scanner.close();

	int count1 = 64, count2 = 64;

	for (int i = 0; i <= N - 8; i++) {
	    for (int j = 0; j <= M - 8; j++) {
		// board1, W
		int count = 0;
		for (int k = i; k < i + 8; k++) {
		    for (int l = j; l < j + 8; l++) {
			if ((k + l) % 2 == 0) {
			    if (board[k].charAt(l) == 'B') {
				count++;
			    }
			} else {
			    if (board[k].charAt(l) == 'W') {
				count++;
			    }
			}
		    }
		}
		if (count1 > count) {
		    count1 = count;
		}

		// board2, B
		count = 0;
		for (int k = i; k < i + 8; k++) {
		    for (int l = j; l < j + 8; l++) {
			if ((k + l) % 2 == 0) {
			    if (board[k].charAt(l) == 'W') {
				count++;
			    }
			} else {
			    if (board[k].charAt(l) == 'B') {
				count++;
			    }
			}
		    }
		}
		if (count2 > count) {
		    count2 = count;
		}
	    }
	}

	System.out.printf("%d", Math.min(count1, count2));
    }
}
