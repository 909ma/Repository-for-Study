/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10988 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String inputString = scanner.nextLine();
	scanner.close();

	int length = inputString.length();
	if (length < 1 || length > 100) {
	    System.out.println("ERROR");
	    return;
	}
	boolean palindrome = true;
	for (int i = 0; i < length; i++) {
	    char c1 = inputString.charAt(i);
	    char c2 = inputString.charAt(length - 1 - i);

	    if (c1 != c2) {
		palindrome = false;
	    }
	}

	if (palindrome) {
	    System.out.println("1");
	} else {
	    System.out.println("0");
	}
    }
}
