/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10798 {

    public static void main(String[] args) {
	final int MAX_X = 5;
	final int MAX_Y = 15;

	Scanner scanner = new Scanner(System.in);
	char[][] inputChar = new char[MAX_X][MAX_Y];

	for (int i = 0; i < MAX_X; i++) {
	    String inputString = scanner.nextLine();
	    int size = inputString.length();

	    if (size > MAX_Y || size < 1) {
		System.out.println("ERROR");
		scanner.close();
		return;
	    }

	    // char[] inputChar[i] = new char[size];
	    for (int j = 0; j < size; j++) {
		inputChar[i][j] = inputString.charAt(j);
	    }
	}
	scanner.close();

	for (int i = 0; i < MAX_Y; i++) {
	    for (int j = 0; j < MAX_X; j++) {
		if (inputChar[j][i] != 0) {
		    System.out.printf("%c", inputChar[j][i]);
		}
	    }
	}
    }
}
