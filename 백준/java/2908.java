/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2908 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int inputString1 = scanner.nextInt();
	int inputString2 = scanner.nextInt();
	if (inputString1 == inputString2) {
	    System.out.println("ERROR");
	    scanner.close();
	    return;
	}
	scanner.close();

	int reverseString1 = 0;
	int reverseString2 = 0;

	for (int i = 0; inputString1 != 0; i++) {
	    reverseString1 = reverseString1 * 10 + inputString1 % 10;
	    inputString1 = inputString1 / 10;
	}
	for (int i = 0; inputString2 != 0; i++) {
	    reverseString2 = reverseString2 * 10 + inputString2 % 10;
	    inputString2 = inputString2 / 10;
	}

	if (reverseString1 > reverseString2) {
	    System.out.println(reverseString1);
	} else {
	    System.out.println(reverseString2);
	}
    }
}
