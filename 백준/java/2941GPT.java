/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 이건 왜 오답이라고 나올까
 */
package practice;

import java.util.Scanner;

public class Java2941GPT {
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

	    if (c == 'c') {
		if (nc == '=' || nc == '-') {
		    count++;
		    i++;
		} else {
		    count++;
		}
	    } else if (c == 'd') {
		if (nc == 'z') {
		    if (i != length - 2) {
			char nnc = inputString.charAt(i + 2);
			if (nnc == '=') {
			    count++;
			    i += 2;
			} else {
			    count++;
			}
		    } else {
			count++;
		    }
		} else if (nc == '-') {
		    count++;
		    i++;
		} else {
		    count++;
		}
	    } else if (c == 'l' || c == 'n') {
		if (nc == 'j') {
		    count++;
		    i++;
		} else {
		    count++;
		}
	    } else if (c == 's' || c == 'z') {
		if (nc == '=') {
		    count++;
		    i++;
		} else {
		    count++;
		}
	    } else {
		count++;
	    }
	}

	System.out.println(count);
    }
}
