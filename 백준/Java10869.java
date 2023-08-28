/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10869 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int A = Scanner.nextInt();
		if(A<1) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		int B = Scanner.nextInt();
		if(B>10000) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		System.out.println(A+B);
		System.out.println(A-B);
		System.out.println(A*B);
		System.out.println(A/B);
		System.out.println(A%B);
	}

}
