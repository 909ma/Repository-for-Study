/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10950 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int Max = Scanner.nextInt();
		int A, B;
		int[] Answer = new int[Max];
		for(int i = 0; i < Max ; i++) {
			A = Scanner.nextInt();
			if(A<=0) {
				System.out.println("ERROR A");
				Scanner.close();
				return;
			}
			B = Scanner.nextInt();
			if(B>=10) {
				System.out.println("ERROR B");
				Scanner.close();
				return;
			}
			Answer[i] = A+B;
		}
		Scanner.close();
		
		for(int i = 0; i < Max ; i++) {
			System.out.println(Answer[i]);
		}
	}

}
