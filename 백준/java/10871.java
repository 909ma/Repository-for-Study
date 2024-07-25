/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10871 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int count = scanner.nextInt();
		if (count < 1 || count > 10000) {
			System.out.println("ERROR count");
			scanner.close();
			return;
		}

		int searchNumber = scanner.nextInt();
		if (searchNumber < 1 || searchNumber > 10000) {
			System.out.println("ERROR searchNumber");
			scanner.close();
			return;
		}

		for (int i = 0; i < count; i++) {
			int number = scanner.nextInt();
			if (number < 1 || number > 10000) {
				System.out.println("ERROR number");
				scanner.close();
				return;
			}
			if (number < searchNumber) {
				System.out.print(number + " ");
			}
		}
		scanner.close();
	}

}
