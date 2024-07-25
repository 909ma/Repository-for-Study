/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2884 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int H = Scanner.nextInt();
		if(H>23||H<0) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		int M = Scanner.nextInt();
		if(M>59||M<0) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		if(M>=45) {
			System.out.println(H + " " + (M-45));
		}
		else {
			if(H>=1) {
				System.out.println((H-1) + " " + (60+M-45));
			}
			else {
				System.out.println(23 + " " + (M+15));
			}
		}
	}

}
