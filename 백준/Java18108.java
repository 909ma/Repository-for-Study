/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java18108 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int Year = Scanner.nextInt();
		Scanner.close();
		Year -= (2541-1998);
		System.out.println(Year);
	}

}
