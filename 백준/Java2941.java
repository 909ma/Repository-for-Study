/*
    @Author   : 909ma
    @Date     : 2023. 5. 22
    @Function : 
 */
package practice;

import java.util.Scanner;

public class Java2941 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String inputString = scanner.nextLine();
	scanner.close();

	int length = inputString.length();
	if (length > 100) {
	    System.out.println("ERROR");
	    return;
	}

	int count = 0;
	for (int i = 0; i < length; i++) {
	    char c = inputString.charAt(i);
	    char nc = (i != length - 1) ? inputString.charAt(i + 1) : '\0';

	    switch (c) {
	    case 'c':
		if (nc == '=') {
		    count++;
		    i++;
		} else if (nc == '-') {
		    count++;
		    i++;
		} else {
		    count++;
		}
		break;
	    case 'd':
		if (nc == 'z') {
		    char nnc = (i != length - 2) ? inputString.charAt(i + 2) : '\0';
		    if (nnc == '=') {
			count++;
			i += 2;
		    }
		} else if (nc == '-') {
		    count++;
		    i++;
		} else {
		    count++;
		}
		break;
	    case 'l':
	    case 'n':
		if (nc == 'j') {
		    count++;
		    i++;
		} else {
		    count++;
		}
		break;
	    case 's':
	    case 'z':
		if (nc == '=') {
		    count++;
		    i++;
		} else {
		    count++;
		}
		break;
	    default:
		count++;
	    }
	}

	System.out.println(count);
    }
}
