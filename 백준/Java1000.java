/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1000 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		
		int A = Scanner.nextInt();
		if(A<=0) {
			System.out.print("Error");
			Scanner.close();
			return;
		}
		
		int B = Scanner.nextInt();
		if(B<=0) {
			System.out.print("Error");
			Scanner.close();
			return;
		}
		
		System.out.printf("%d", A+B);
		Scanner.close();//메모리 누수 방지
	}

}
