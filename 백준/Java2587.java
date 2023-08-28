/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java2587 {

    public static void main(String[] args) {
	final int NUMBER_MAX = 5;
	Scanner scanner = new Scanner(System.in);
	int[] number = new int[5];
	for (int i = 0; i < NUMBER_MAX; i++) {
	    number[i] = scanner.nextInt();
	}
	scanner.close();

	Arrays.sort(number);
	int sum = 0;
	for (int i = 0; i < NUMBER_MAX; i++) {
	    sum += number[i];
	}
	double avg = (double) sum / NUMBER_MAX;

	System.out.printf("%d\n", (int) avg);
	System.out.println(number[2]);
    }
}
