/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10810 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int numberSize = scanner.nextInt();
		if(numberSize < 1 || numberSize > 100) {
			System.out.println("ERROR numberSize");
			scanner.close();
			return;
		}
		int numberCycle = scanner.nextInt();
		if(numberCycle < 1 || numberCycle > 100) {
			System.out.println("ERROR numberCycle");
			scanner.close();
			return;
		}
		int[] numberList = new int[numberSize];
		int startNumber, endNumber, inputNumber;
		for(int i = 0; i < numberCycle ; i++) {
			startNumber = scanner.nextInt();
			if(startNumber < 1 || startNumber > numberSize) {
				System.out.println("ERROR");
				scanner.close();
				return;
			}
			endNumber = scanner.nextInt();
			if(endNumber < 1 || endNumber > numberSize) {
				System.out.println("ERROR");
				scanner.close();
				return;
			}
			inputNumber = scanner.nextInt();
			if(inputNumber < 1 || inputNumber > numberSize) {
				System.out.println("ERROR");
				scanner.close();
				return;
			}
			for(int j = startNumber ; j <= endNumber ; j++) {
				numberList[j-1] = inputNumber;
			}
		}
		scanner.close();
		
		for(int i = 0 ; i < numberSize ; i++) {
			System.out.print(numberList[i] + " ");
		}
	}
}
