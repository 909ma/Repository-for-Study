/*
	@Author   : 909ma
	@Date     : 2023. 5. 17
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10926 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		String Name = Scanner.nextLine();
		Scanner.close();//메모리 누수 방지
		
		System.out.println(Name + "??!");
	}

}
