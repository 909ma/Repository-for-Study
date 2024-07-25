/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java11718GPT {
    public static void main(String[] args) {
	final int MAX_NUMBER = 100;
	String[] inputString = new String[MAX_NUMBER];

	Scanner scanner = new Scanner(System.in);
	int index = 0;
	while (scanner.hasNextLine()) {
	    String line = scanner.nextLine();
	    if (line.isEmpty()) {
		break;
	    }
	    inputString[index] = line;
	    index++;
	}
	scanner.close();

	for (String str : inputString) {
	    if (str == null) {
		break;
	    }
	    System.out.println(str);
	}
    }
}
