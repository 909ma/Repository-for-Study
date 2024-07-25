/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java4344 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int testCase = scanner.nextInt();
	if (testCase < 1) {
	    System.out.println("ERROR");
	    scanner.close();
	    return;
	}

	int[] people = new int[testCase];
	int[][] score = new int[testCase][];
	double[] avg = new double[testCase];

	for (int i = 0; i < testCase; i++) {
	    people[i] = scanner.nextInt();
	    if (people[i] < 1 || people[i] > 1000) {
		System.out.println("ERROR");
		scanner.close();
		return;
	    }

	    score[i] = new int[people[i]];

	    for (int j = 0; j < people[i]; j++) {
		score[i][j] = scanner.nextInt();
		if (score[i][j] < 0 || score[i][j] > 100) {
		    System.out.println("ERROR");
		    scanner.close();
		    return;
		}
		avg[i] += score[i][j];
	    }
	    avg[i] = avg[i] / people[i];
	}
	scanner.close();

	int[] upPeople = new int[testCase];
	Arrays.fill(upPeople, 0);

	for (int i = 0; i < testCase; i++) {
	    for (int j = 0; j < people[i]; j++) {
		if (score[i][j] > avg[i]) {
		    upPeople[i]++;
		}
	    }
	}

	for (int i = 0; i < testCase; i++) {
	    System.out.printf("%.3f%%\n", (float) upPeople[i] / people[i] * 100);
	}
    }
}
