/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java8393 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int n = Scanner.nextInt();
		if(n > 10000|| n < 1) {
			System.out.println("ERROR n");
			Scanner.close();
			return;
		}
		Scanner.close();
		int answer = 0;
		for(int i = 0; i < n ; i++) {
			answer += i+1;
		}
		System.out.println(answer);
	}

}
