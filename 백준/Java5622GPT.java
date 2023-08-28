/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java5622GPT {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String phoneNumber = scanner.nextLine();
	scanner.close();

	int time = 0;

	for (int i = 0; i < phoneNumber.length(); i++) {
	    char c = phoneNumber.charAt(i);
	    time += getTimeForCharacter(c);
	}

	System.out.println(time);
    }

    private static int getTimeForCharacter(char c) {
	switch (c) {
	case 'A':
	case 'B':
	case 'C':
	    return 3;
	case 'D':
	case 'E':
	case 'F':
	    return 4;
	case 'G':
	case 'H':
	case 'I':
	    return 5;
	case 'J':
	case 'K':
	case 'L':
	    return 6;
	case 'M':
	case 'N':
	case 'O':
	    return 7;
	case 'P':
	case 'Q':
	case 'R':
	case 'S':
	    return 8;
	case 'T':
	case 'U':
	case 'V':
	    return 9;
	case 'W':
	case 'X':
	case 'Y':
	case 'Z':
	    return 10;
	default:
	    return 0;
	}
    }
}
