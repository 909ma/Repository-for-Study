/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1157GPT {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String inputString = scanner.nextLine().toUpperCase(); // 입력 문자열을 대문자로 변환
	scanner.close();

	int[] characterList = new int[26];

	for (int i = 0; i < inputString.length(); i++) {
	    char c = inputString.charAt(i);
	    if (Character.isAlphabetic(c)) { // 알파벳인 경우에만 처리
		characterList[c - 'A']++; // 대문자로 변환되었으므로 'A'를 빼서 인덱스로 사용
	    }
	}

	int maxNumber = 0;
	boolean unique = true;
	char maxChar = '?';

	for (int i = 0; i < 26; i++) {
	    if (characterList[i] > maxNumber) {
		maxNumber = characterList[i];
		maxChar = (char) (i + 'A'); // 대문자로 출력하기 위해 'A'를 더함
		unique = true;
	    } else if (characterList[i] == maxNumber) {
		unique = false;
	    }
	}

	if (unique) {
	    System.out.println(maxChar);
	} else {
	    System.out.println("?");
	}
    }
}
