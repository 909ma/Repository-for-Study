/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1008 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		double A = Scanner.nextDouble();
		if(A<=0) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		double B = Scanner.nextDouble();
		if(B>=10) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		System.out.println(A/B);
	}

}
