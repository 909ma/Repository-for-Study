/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2588 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int A = Scanner.nextInt();
		if(A<100||A>999) {
			System.out.print("Error");
			Scanner.close();
			return;
		}
		int B = Scanner.nextInt();
		if(B<100||B>999) {
			System.out.print("Error");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		int B1, B2, B3;
		B1 = B%10;
		B2 = (B-B1)/10%10;
		B3 = (B-B%100)/100;

		System.out.println(A*B1);
		System.out.println(A*B2);
		System.out.println(A*B3);
		System.out.println(A*B);
		
	}

}
