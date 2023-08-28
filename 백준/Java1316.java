/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
	
	틀린 로직
import java.util.Arrays;
import java.util.Scanner;

public class Java1316 {
    public static void main(String[] args) {
	int count = 0;
	Scanner scanner = new Scanner(System.in);
	int numberOfString = scanner.nextInt();
	if (numberOfString > 100 || numberOfString < 1) {
	    System.out.println("ERROR");
	    scanner.close();
	    return;
	}
	scanner.nextLine();
	String[] inputString = new String[numberOfString];

	for (int i = 0; i < numberOfString; i++) {
	    inputString[i] = scanner.nextLine();
	}
	scanner.close();
	int[] alphabetList = new int[26];
	Arrays.fill(alphabetList, 0);
	boolean check = true;
	boolean continuity = false;

	for (int i = 0; i < numberOfString; i++) {
	    int size = inputString[i].length();
	    for (int j = 0; j < size - 1; j++) {
		char c = inputString[i].charAt(j);
		char nc = inputString[i].charAt(j + 1);

		if (alphabetList[(int) c - 10] == 0) {
		    alphabetList[(int) c - 10]++;
		    if (j != size - 1 && (c == nc)) {
			continuity = true;
			i++;
		    }
		} else if (continuity) {
		    if (j != size - 1 && (c == nc)) {
			i++;
		    } else {
			continuity = false;
		    }
		} else {
		    check = false;
		    break;
		}
	    }
	    if (check) {
		count++;
	    }
	    Arrays.fill(alphabetList, 0);
	}

	System.out.println(count);

    }
}
 */
package practice;

import java.util.Scanner;

public class Java1316 {
    public static void main(String[] args) {
	int count = 0;
	Scanner scanner = new Scanner(System.in);
	int numberOfString = scanner.nextInt();
	if (numberOfString > 100 || numberOfString < 1) {
	    System.out.println("ERROR");
	    scanner.close();
	    return;
	}
	scanner.nextLine();

	for (int i = 0; i < numberOfString; i++) {
	    String inputString = scanner.nextLine();
	    boolean[] visited = new boolean[26];
	    boolean isGroupWord = true;

	    for (int j = 0; j < inputString.length(); j++) {
		char c = inputString.charAt(j);

		if (visited[c - 'a']) {
		    if (c != inputString.charAt(j - 1)) {
			isGroupWord = false;
			break;
		    }
		} else {
		    visited[c - 'a'] = true;
		}
	    }

	    if (isGroupWord) {
		count++;
	    }
	}

	scanner.close();
	System.out.println(count);
    }
}
