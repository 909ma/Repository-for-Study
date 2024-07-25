/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1427 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String input = scanner.nextLine();
	scanner.close();

	int[] list = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	StringBuilder sb = new StringBuilder();

	int length = input.length();
	for (int i = 0; i < length; i++) {
	    int number = (int) input.charAt(i) - 48;
	    list[number]++;
	}
	for (int i = 9; i >= 0;) {
	    if (list[i] != 0) {
		sb.append(i);
		list[i]--;
	    } else {
		{
		    i--;
		}
	    }

	}
	System.out.println(sb);
    }
}
