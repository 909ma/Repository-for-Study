/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java11654 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		char inputChar = scanner.nextLine().charAt(0);
		scanner.close();
		System.out.printf("%d", (int)inputChar);
	}
}
