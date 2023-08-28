/*
 * @Author : 909ma
 * 
 * @Date : 2023. 5. 21
 * 
 * @Function :
 */

package practice;

import java.util.Scanner;

public class Java2675GPT {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);

	int testCase = scanner.nextInt();
	if (testCase < 1 || testCase > 1000) {
	    System.out.println("ERROR");
	    scanner.close();
	    return;
	}
	scanner.nextLine(); // Consume the newline character

	for (int i = 0; i < testCase; i++) {
	    int repeat = scanner.nextInt();
	    if (repeat < 1 || repeat > 8) {
		System.out.println("ERROR");
		scanner.close();
		return;
	    }
	    String inputString = scanner.next();
	    if (inputString.length() > 20 || inputString.length() < 1) {
		System.out.println("ERROR");
		scanner.close();
		return;
	    }

	    StringBuilder result = new StringBuilder();
	    for (int j = 0; j < inputString.length(); j++) {
		char ch = inputString.charAt(j);
		for (int k = 0; k < repeat; k++) {
		    result.append(ch);
		}
	    }
	    System.out.println(result);
	}

	scanner.close();
    }
}
