/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java5597GPT2 {
    public static void main(String[] args) {
        final int TOTAL_STUDENTS = 30; // 총 학생 수
        final int MISSING_STUDENTS = 2; // 제출하지 않은 학생 수

        // 학생 제출 여부 초기화
        int[] submissionStatus = new int[TOTAL_STUDENTS];
        Arrays.fill(submissionStatus, 0);

        // 학생 과제 제출 여부 입력받기
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < TOTAL_STUDENTS - MISSING_STUDENTS; i++) {
            int studentNumber = scanner.nextInt();
            if (!isValidStudentNumber(studentNumber, 1, TOTAL_STUDENTS)) {
                System.out.println("ERROR");
                scanner.close();
                return;
            }
            if (submissionStatus[studentNumber - 1] == 0) {
                submissionStatus[studentNumber - 1] = 1;
            } else {
                System.out.println("중복 입력");
                scanner.close();
                return;
            }
        }
        scanner.close();

        // 결과 출력
        for (int i = 0; i < TOTAL_STUDENTS; i++) {
            if (submissionStatus[i] == 0) {
                System.out.println(i + 1);
            }
        }
    }

    private static boolean isValidStudentNumber(int number, int minNumber, int maxNumber) {
        return number >= minNumber && number <= maxNumber;
    }
}
