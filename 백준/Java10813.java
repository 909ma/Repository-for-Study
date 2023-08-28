/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10813 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int numberSize = scanner.nextInt();
		if(numberSize < 1 || numberSize > 100) {
			System.out.println("ERROR numberSize");
			scanner.close();
			return;
		}
		int tryTimes = scanner.nextInt();
		if(tryTimes < 1 || tryTimes > 100) {
			System.out.println("ERROR tryTimes");
			scanner.close();
			return;
		}
		
		//컵에 공 넣기
		int[] numberCup = new int[numberSize];
		for(int i = 0; i < numberSize ; i++) {
			numberCup[i] = i+1;
		}
		
		//컵 안에 든 공 바꾸기
		for(int i = 0 ; i < tryTimes ; i++) {
			int startNumber = scanner.nextInt();
			int temp;
			if(startNumber < 1 || startNumber > numberSize) {
				System.out.println("ERROR startNUmber");
				scanner.close();
				return;
			}
			
			int endNumber = scanner.nextInt();
			if(endNumber < startNumber || endNumber > numberSize) {
				System.out.println("ERROR endSNumber");
				scanner.close();
				return;
			}
			temp = numberCup[startNumber-1];
			numberCup[startNumber-1] = numberCup[endNumber-1];
			numberCup[endNumber-1] = temp;
		}
		scanner.close();
		
		//결과 출력
		for(int i = 0; i < numberSize ; i++) {
			System.out.print(numberCup[i] + " ");
		}
	}
}
