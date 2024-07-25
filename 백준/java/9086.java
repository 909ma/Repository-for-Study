/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java9086 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int count = scanner.nextInt();
		if(count < 1 || count > 10) {
			System.out.println("ERROR");
			scanner.close();
			return;
		}
		scanner.nextLine();
		
		String[] inputString = new String[count];
		for(int i = 0; i < count; i++) {
			inputString[i]= scanner.nextLine();
			if(inputString[i].length()>=1000) {
				System.out.println("ERROR");
				scanner.close();
				return;
			}
		}
		scanner.close();
		
		for(int i = 0; i < count ; i++) {
			System.out.print(inputString[i].charAt(0));
			System.out.print(inputString[i].charAt(inputString[i].length()-1));
			System.out.println();
		}
		
	}
}
