/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2753 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int Year = Scanner.nextInt();
		if(Year<1||Year>4000) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		if(Year%4 == 0) {
			if((Year%100 != 0)||(Year%400 == 0)) {
				System.out.println(1);
			}
			else {
				System.out.println(0);
			}
		}
		else {
			System.out.println(0);
		}
	}

}
