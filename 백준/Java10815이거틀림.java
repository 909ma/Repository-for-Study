/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java10815이거틀림 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	int[] card = new int[N];
	for (int i = 0; i < N; i++) {
	    card[i] = scanner.nextInt();
	}
	int M = scanner.nextInt();
	int[] checkCard = new int[M];
	for (int i = 0; i < M; i++) {
	    checkCard[i] = scanner.nextInt();
	}
	scanner.close();
	int[] check = new int[M];
	Arrays.fill(check, 0);
	for (int i = 0; i < M; i++) {
	    for (int j = 0; j < N; j++) {
		if (card[j] == checkCard[i]) {
		    check[i]++;
		    break;
		}
	    }
	}

	for (int i = 0; i < M; i++) {
	    System.out.printf("%d ", check[i]);
	}
    }
}
