/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java14215 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int a = scanner.nextInt();
	int b = scanner.nextInt();
	int c = scanner.nextInt();
	scanner.close();

	if (a >= b + c) {
	    System.out.println(b + b + c + c - 1);
	} else if (b >= a + c) {
	    System.out.println(a + a + c + c - 1);

	} else if (c >= a + b) {
	    System.out.println(b + b + a + a - 1);
	} else {
	    System.out.println(a + b + c);
	}
    }
}
