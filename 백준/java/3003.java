/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java3003 {
    public static void main(String[] agrs) {
	int[] inputNumber = new int[6];
	int[] numberOfPieces = { 1, 1, 2, 2, 2, 8 };
	Scanner scanner = new Scanner(System.in);
	for (int i = 0; i < 6; i++) {
	    inputNumber[i] = scanner.nextInt();
	    if (inputNumber[i] < 0 || inputNumber[i] > 10) {
		System.out.println("ERROR");
		scanner.close();
		return;
	    }
	}
	scanner.close();

	for (int i = 0; i < 6; i++) {
	    System.out.printf("%d ", numberOfPieces[i] - inputNumber[i]);
	}
    }
}
