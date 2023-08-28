/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1001 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int A = Scanner.nextInt();
		if(A<=0) {
			System.out.print("ERROR");
			Scanner.close();
			return;
		}
		int B = Scanner.nextInt();
		if(B>=10) {
			System.out.print("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		System.out.print(A-B);
	}

}
