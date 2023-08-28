/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2562 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		final int MAX_COUNT = 9;
		int[] numberList = new int[MAX_COUNT];
		for(int i = 0; i < MAX_COUNT ; i++) {
			numberList[i] = scanner.nextInt();
			for(int j = 0; j < i ; j++) {
				if(numberList[i] == numberList[j]) {
					System.out.println("중복 에러");
					scanner.close();
					return;
				}
			}
			if(numberList[i]<1 || numberList[i] >= 100) {
				System.out.println("ERROR numberList[" + i + "]");
				scanner.close();
				return;
			}
		}
		scanner.close();
		int index = 0;
		int maxValue = numberList[0];
		for(int i = 0; i < MAX_COUNT ; i++) {
			if(maxValue < numberList[i]) {
				maxValue = numberList[i];
				index = i;
			}
		}
		System.out.println(maxValue);
		System.out.println(index+1);
	}
}
