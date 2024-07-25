/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java11005GPT {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int number = scanner.nextInt();
	int base = scanner.nextInt();

	if (base < 2 || base > 36) {
	    System.out.println("ERROR base");
	    scanner.close();
	    return;
	}
	scanner.close();

	String result = convertToBaseN(number, base);
	System.out.println(result);
    }

    public static String convertToBaseN(int number, int base) {
	StringBuilder sb = new StringBuilder();
	while (number > 0) {
	    int remainder = number % base;
	    char digit;
	    if (remainder < 10) {
		digit = (char) (remainder + '0');
	    } else {
		digit = (char) (remainder - 10 + 'A');
	    }
	    sb.insert(0, digit);
	    number /= base;
	}
	return sb.toString();
    }
}
