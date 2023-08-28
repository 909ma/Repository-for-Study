/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2798GPT {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	if (N < 3 || N > 100) {
	    System.out.println("ERROR N");
	    scanner.close();
	    return;
	}

	int M = scanner.nextInt();
	if (M < 10 || M > 300000) {
	    System.out.println("ERROR M");
	    scanner.close();
	    return;
	}

	int[] cardList = new int[N];
	for (int i = 0; i < N; i++) {
	    cardList[i] = scanner.nextInt();
	    if (cardList[i] > 100000 || cardList[i] < 1) {
		System.out.println("ERROR cardList[" + i + "]");
		scanner.close();
		return;
	    }
	}
	scanner.close();

	int closestSum = findClosestSum(cardList, N, M);
	System.out.println(closestSum);
    }

    public static int findClosestSum(int[] cardList, int N, int M) {
	int closestSum = 0;
	int minDiff = Integer.MAX_VALUE;

	for (int i = 0; i < N - 2; i++) {
	    for (int j = i + 1; j < N - 1; j++) {
		for (int k = j + 1; k < N; k++) {
		    int sum = cardList[i] + cardList[j] + cardList[k];
		    int diff = Math.abs(M - sum);
		    if (diff < minDiff) {
			minDiff = diff;
			closestSum = sum;
		    }
		}
	    }
	}

	return closestSum;
    }
}
