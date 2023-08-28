/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java9498 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int Score = Scanner.nextInt();
		if(Score<0||Score>100) {
			System.out.println("ERROR");
			Scanner.close();
			return;
		}
		Scanner.close();
		
		if(Score>=90) {
			System.out.println("A");
		}
		else if(Score>=80) {
			System.out.println("B");
		}
		else if(Score>=70) {
			System.out.println("C");
		}
		else if(Score>=60) {
			System.out.println("D");
		}
		else {
			System.out.println("F");
		}
	}

}
