/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java5622 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String phoneNumber = scanner.nextLine();
	scanner.close();

	int time = 0;

	for (int i = 0; i < phoneNumber.length(); i++) {
	    char c = phoneNumber.charAt(i);
	    switch (c) {
	    case 'A':
	    case 'B':
	    case 'C':
		time += 3;
		break;
	    case 'D':
	    case 'E':
	    case 'F':
		time += 4;
		break;
	    case 'G':
	    case 'H':
	    case 'I':
		time += 5;
		break;
	    case 'J':
	    case 'K':
	    case 'L':
		time += 6;
		break;
	    case 'M':
	    case 'N':
	    case 'O':
		time += 7;
		break;
	    case 'P':
	    case 'Q':
	    case 'R':
	    case 'S':
		time += 8;
		break;
	    case 'T':
	    case 'U':
	    case 'V':
		time += 9;
		break;
	    case 'W':
	    case 'X':
	    case 'Y':
	    case 'Z':
		time += 10;
		break;
	    }
	}

	System.out.println(time);
    }
}
