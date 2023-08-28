/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2739 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int number = Scanner.nextInt();
		if(number <1 || number >9) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		for(int i = 1; i <= 9 ; i++) {
			System.out.println(number + " * " + i + " = " + number*i);
		}
	}

}
