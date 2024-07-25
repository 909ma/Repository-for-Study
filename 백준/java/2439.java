/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2439 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int N = Scanner.nextInt();
		if(N<1||N>100) {
			System.out.println("ERROR N");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		for(int i = 1; i<=N; i++) {
			for(int k = 0; k < N-i;k++ ) {
				System.out.print(" ");
			}
			for(int j = 0; j<i ; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}

}
