/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
	https://www.acmicpc.net/problem/2525
 */
package practice;

import java.util.Scanner;

public class Java2525 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int A = Scanner.nextInt();
		if(A<0||A>23) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		int B = Scanner.nextInt();
		if(B<0||B>59) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		int C = Scanner.nextInt();
		if(C<0||C>1000) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		B += C%60;
		A += B/60 + C/60;
		A %= 24;
		B %= 60;
		
		System.out.println(A + " " + B);
	}

}
