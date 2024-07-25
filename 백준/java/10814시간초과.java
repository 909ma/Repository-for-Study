/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10814시간초과 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int count = Integer.parseInt(scanner.nextLine());
	int[] age = new int[count];
	String[] name = new String[count];

	for (int i = 0; i < count; i++) {
	    String[] line = scanner.nextLine().split(" ");
	    age[i] = Integer.parseInt(line[0]);
	    name[i] = line[1];
	}
	scanner.close();

	for (int i = 1; i < count; i++) {
	    for (int j = i; j < count; j++) {
		if (age[j] < age[j - 1]) {
		    int tempAge = age[j];
		    String tempName = name[j];
		    age[j] = age[j - 1];
		    name[j] = name[j - 1];
		    age[j - 1] = tempAge;
		    name[j - 1] = tempName;
		    i = 0;
		}
	    }
	}

	for (int i = 0; i < count; i++) {
	    System.out.printf("%s %s\n", age[i], name[i]);
	}
    }
}
