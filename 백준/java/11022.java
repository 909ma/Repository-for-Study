/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java11022 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int count = Scanner.nextInt();
		if (count < 0) {
			System.out.println("ERROR count");
			Scanner.close();
			return;
		}
		int[] A = new int[count];
		int[] B = new int[count];
		for (int i = 0; i < count; i++) {
			A[i] = Scanner.nextInt();
			if (A[i] <= 0) {
				System.out.println("ERROR A");
				Scanner.close();
				return;
			}
			B[i] = Scanner.nextInt();
			if (B[i] >= 10) {
				System.out.println("ERROR B");
				Scanner.close();
				return;
			}
		}

		Scanner.close();
		for (int i = 0; i < count; i++) {
			System.out.println("Case #" + (i + 1) + ": " + A[i] + " + " + B[i] + " = " + (A[i] + B[i]));
		}
	}

}
