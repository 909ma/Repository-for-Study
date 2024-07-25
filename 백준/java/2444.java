/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2444 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int number = scanner.nextInt();
	scanner.close();

	for (int i = 0; i < number; i++) {
	    for (int j = 0; j < number - (i + 1); j++) {
		System.out.print(" ");
	    }
	    for (int j = 0; j <= 2 * i; j++) {
		System.out.print("*");
	    }
	    System.out.println();
	}
	for (int i = 0; i < number - 1; i++) {
	    for (int j = 0; j < (i + 1); j++) {
		System.out.print(" ");
	    }
	    for (int j = 0; j <= 2 * (number - (i + 2)); j++) {
		System.out.print("*");
	    }
	    System.out.println();
	}
    }
}
