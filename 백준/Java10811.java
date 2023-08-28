/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10811 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		//바구니 갯수 입력
		int cupSize = scanner.nextInt();
		if(cupSize < 1 || cupSize > 100) {
			System.out.println("ERROR");
			scanner.close();
			return;
		}
		
		//바구니 채워넣기
		int[] cupList = new int[cupSize];
		int[] reverseCupList = new int[cupSize];
		for(int i = 1; i <= cupSize ; i++) {
			cupList[i-1] = i;
			reverseCupList[i-1] = i;
		}
		//reverseCupList = cupList;//이게 문법적으로 되던가
		
		//바꿀 횟수 입력
		int change = scanner.nextInt();
		if(change < 1 || change > 100) {
			System.out.println("ERROR");
			scanner.close();
			return;
		}
		
		//바구니 위치 바꾸기
		for(int i = 0; i < change ; i++) {
			int start = scanner.nextInt();
			if(start < 1 || start > cupSize) {
				System.out.println("ERROR");
				scanner.close();
				return;
			}
			
			int end = scanner.nextInt();
			if(end < start || end > cupSize) {
				System.out.println("ERROR");
				scanner.close();
				return;
			}
			
			//진짜 바꾸기
			for(int j = 0 ; j <= end-start ; j++) {
				reverseCupList[start-1+j] = cupList[end-1-j];
			}
			for(int j = 0 ; j < cupSize ; j++) {
				cupList[j] = reverseCupList[j];
			}
		}
		scanner.close();
		
		for(int i = 0; i < cupSize; i++) {
			System.out.print(cupList[i] + " ");
		}
	}
}
