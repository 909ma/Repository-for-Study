/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2480 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		//첫번째 숫자 입력
		int A = Scanner.nextInt();
		if(A<1||A>6) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		//두번째 숫자 입력
		int B = Scanner.nextInt();
		if(B<1||B>6) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		//세번째 숫자 입력
		int C = Scanner.nextInt();
		if(C<1||C>6) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		//같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
		if(A==B&&A==C) {
			System.out.println(10000+A*1000);
		}
		//같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
		else if((A==B&&A!=C)||(A!=B&&A==C)) {
			System.out.println(1000+A*100);
		}
		else if(B==C&&A!=B) {
			System.out.println(1000+B*100);
		}
		else {
			if(A>B&&A>C) {
				System.out.println(A*100);
			}
			else if(B>C&&B>A) {
				System.out.println(B*100);
			}
			else {
				System.out.println(C*100);
			}
		}
		
	}

}
