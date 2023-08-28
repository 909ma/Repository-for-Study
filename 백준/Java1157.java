/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java1157 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String inputString = scanner.nextLine().toUpperCase();
	scanner.close();

	int length = inputString.length();
	if (length > 1000000) {
	    System.out.println("ERROR");
	    return;
	}

	boolean unique = true;
	// A는 65, Z는90
	int[] characterList = new int[26];
	Arrays.fill(characterList, 0);

	for (int i = 0; i < length; i++) {
	    characterList[(int) inputString.charAt(i) - 65]++;
	}

	int maxNumber = 0;
	for (int i = 0; i < 26; i++) {
	    if (characterList[i] > maxNumber) {
		maxNumber = characterList[i];
	    }
	}

	boolean max = false;
	int index = 0;
	for (int i = 0; i < 26; i++) {
	    if (characterList[i] == maxNumber && max == false) {
		max = true;
		index = i;
	    } else if (characterList[i] == maxNumber && max == true) {
		unique = false;
	    }
	}

	if (unique) {
	    System.out.printf("%c", (char) (index + 65));
	} else {
	    System.out.println("?");
	}
    }
}
