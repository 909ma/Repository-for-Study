/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java25206 {
    public static void main(String[] args) {
	final int NUMBER_OF_SUBJECT = 20;
	Scanner scanner = new Scanner(System.in);
	String[] subjectName = new String[NUMBER_OF_SUBJECT];
	double[] subjectUnit = new double[NUMBER_OF_SUBJECT];
	String[] subjectScore = new String[NUMBER_OF_SUBJECT];
	double[] subjectScoreNumber = new double[NUMBER_OF_SUBJECT];
	for (int i = 0; i < NUMBER_OF_SUBJECT; i++) {
	    String line = scanner.nextLine();
	    String[] parts = line.split(" ");
	    subjectName[i] = parts[0];
	    subjectUnit[i] = Double.parseDouble(parts[1]);
	    subjectScore[i] = parts[2];
	}
	scanner.close();

	for (int i = 0; i < NUMBER_OF_SUBJECT; i++) {
	    switch (subjectScore[i]) {
	    case "A+":
		subjectScoreNumber[i] = 4.5;
		break;
	    case "A0":
		subjectScoreNumber[i] = 4.0;
		break;
	    case "B+":
		subjectScoreNumber[i] = 3.5;
		break;
	    case "B0":
		subjectScoreNumber[i] = 3.0;
		break;
	    case "C+":
		subjectScoreNumber[i] = 2.5;
		break;
	    case "C0":
		subjectScoreNumber[i] = 2.0;
		break;
	    case "D+":
		subjectScoreNumber[i] = 1.5;
		break;
	    case "D0":
		subjectScoreNumber[i] = 1.0;
		break;
	    case "F":
		subjectScoreNumber[i] = 0;
		break;
	    case "P":
		subjectScoreNumber[i] = -1;
		break;
	    }
	}

	double sum = 0;
	double sumUnit = 0;

	for (int i = 0; i < NUMBER_OF_SUBJECT; i++) {
	    if (subjectScoreNumber[i] != -1) {
		sum += subjectUnit[i] * subjectScoreNumber[i];
	    }
	}
	for (int i = 0; i < NUMBER_OF_SUBJECT; i++) {
	    if (subjectScoreNumber[i] != -1) {
		sumUnit += subjectUnit[i];
	    }
	}
	double avg = sum / sumUnit;

	// System.out.println(sum);
	// System.out.println(sumUnit);
	System.out.println(avg);
    }
}
