/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java5597 {
	public static void main(String[] args) {
		final int STUDENT_SIZE = 30;//총 인원
		final int STUDENT_NO = 2;//안 낸 놈
		//학생 리스트 초기화
		int[] studentList = new int[STUDENT_SIZE];
		for(int i = 0; i < STUDENT_SIZE ; i++) {
			studentList[i] = 0;
		}
		
		//학생 과제 제출 유무 입력받기
		Scanner scanner = new Scanner(System.in);
		for(int i = 0; i < STUDENT_SIZE - STUDENT_NO ; i++) {
			int temp = scanner.nextInt();
			if(temp < 1 || temp > STUDENT_SIZE) {
				System.out.println("ERROR");
				scanner.close();
				return;
			}
			if(studentList[temp-1] == 0) {
				studentList[temp-1] = 1;
			}
			else {
				System.out.println("중복 입력");
				scanner.close();
				return;
			}
		}
		scanner.close();
		for(int i = 0; i < STUDENT_SIZE; i++) {
			if(studentList[i] == 0) {
				System.out.println(i+1);
			}
			else {
				continue;
			}
		}
	}
}
