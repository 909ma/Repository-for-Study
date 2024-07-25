/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : GPT 도움 받았음
 */

package practice;

import java.util.Scanner;

public class Java1152 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String inputString = scanner.nextLine();
	scanner.close();

	int wordCount = 0;
	boolean isWord = false;

	for (int i = 0; i < inputString.length(); i++) {
	    char c = inputString.charAt(i);

	    if (c != ' ') {
		// 이전 문자가 공백인 경우 단어 개수 증가
		if (!isWord) {
		    wordCount++;
		    isWord = true;
		}
	    } else {
		// 공백인 경우 단어 종료
		isWord = false;
	    }
	}

	System.out.println(wordCount);
    }
}
