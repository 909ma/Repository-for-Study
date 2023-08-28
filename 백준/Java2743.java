/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2743 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String inputString = scanner.nextLine();
		if(inputString.length()>100) {
			System.out.println("ERROR");
			scanner.close();
			return;
		}
		scanner.close();
		
		System.out.println(inputString.length());
	}
}
