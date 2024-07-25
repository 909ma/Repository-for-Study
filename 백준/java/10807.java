/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10807 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int count = Scanner.nextInt();
		if(count < 1 || count > 100) {
			System.out.println("ERROR count");
			Scanner.close();
			return;
		}
		
		int[] numberList = new int[count];
		for(int i = 0; i < count; i++) {
			numberList[i] = Scanner.nextInt();
			if(numberList[i] < -100 || numberList[i] > 100) {
				System.out.println("ERROR numberList[" + i + "]");
				Scanner.close();
				return;
			}
		}
		int searchNumber = Scanner.nextInt();
		if(searchNumber < -100 || searchNumber > 100) {
			System.out.println("ERROR searchNumber");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		int countNumber = 0;
		for(int i = 0; i < count ; i++) {
			if(searchNumber == numberList[i]) {
				countNumber++;
			}
		}
		System.out.println(countNumber);
	}

}
