/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10430 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int A = Scanner.nextInt();
		int B = Scanner.nextInt();
		int C = Scanner.nextInt();
		Scanner.close();

		System.out.println((A+B)%C);
		System.out.println(((A%C) + (B%C))%C);
		System.out.println( (A*B)%C);
		System.out.println(((A%C) * (B%C))%C);
	}

}
