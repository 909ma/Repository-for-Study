/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java1181 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = Integer.parseInt(scanner.nextLine());
	String[] inputString = new String[N];
	for (int i = 0; i < N; i++) {
	    inputString[i] = scanner.nextLine();
	}
	scanner.close();
	Arrays.sort(inputString);

	int max = 0;

	for (int i = 0; i < N; i++) {
	    int length = inputString[i].length();
	    if (max < length) {
		max = length;
	    }
	}

	// 중복 제거
	int newSize = 0;
	String[] distinctStrings = new String[N];
	distinctStrings[newSize++] = inputString[0];

	for (int i = 1; i < N; i++) {
	    if (!inputString[i].equals(inputString[i - 1])) {
		distinctStrings[newSize++] = inputString[i];
	    }
	}

	// 중복 제거된 배열로 대체
	inputString = Arrays.copyOf(distinctStrings, newSize);

	for (int count = 1; count <= max; count++) {
	    for (int i = 0; i < inputString.length; i++) {
		if (count == inputString[i].length()) {
		    System.out.println(inputString[i]);
		}
	    }
	}
    }
}
