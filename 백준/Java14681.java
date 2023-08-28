/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java14681 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int x = Scanner.nextInt();
		if(x>1000||x<-1000||x==0) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		
		int y = Scanner.nextInt();
		if(y>1000||y<-1000||y==0) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		if(x>0) {
			if(y>0) {
				System.out.println(1);
			}
			else {
				System.out.println(4);
			}
		}
		else {
			if(y>0) {
				System.out.println(2);
			}
			else {
				System.out.println(3);
			}
		}
	}

}
