/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10818 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int count = scanner.nextInt();
		if(count < 1 || count > 1000000) {
			System.out.println("ERROR count");
			scanner.close();
			return;
		}
		int[] numberList = new int[count];
		for(int i = 0; i < count ; i ++) {
			numberList[i] = scanner.nextInt();
			if(numberList[i]<-1000000 || numberList[i] > 1000000) {
				System.out.println("ERROR numberList[" + i + "]");
				scanner.close();
				return;
			}
		}
		scanner.close();
		int min = numberList[0];
		int max = numberList[0];
		//search min
		for(int i = 0; i < count ; i++) {
			if(min > numberList[i]) {
				min = numberList[i];
			}
		}
		//search max
		for(int i = 0; i < count ; i++) {
			if(max < numberList[i]) {
				max = numberList[i];
			}
		}
		System.out.println(min + " " + max);
	}

}
