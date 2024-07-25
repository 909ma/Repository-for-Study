/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java3052 {
	public static void main(String[] args) {
		final int NUMBER_SIZE = 10;
		final int MAX_NUMBER = 42;
		
		//나머지를 저장할 리스트
		int[] remainList = new int[42];
		Arrays.fill(remainList,  0);
		
		//나머지가 나온 횟수를 리스트에 저장
		Scanner scanner = new Scanner(System.in);
		for(int i = 0; i < NUMBER_SIZE ; i++) {
			int temp = scanner.nextInt();
			if(temp < 0 || temp > 1000) {
				System.out.println("ERROR temp");
				scanner.close();
				return;
			}
			remainList[temp%42]++;
		}
		scanner.close();
		
		//서로 다른 나머지 개수 세아리기
		int answer = 0;
		for(int i = 0; i < MAX_NUMBER ; i++) {
			if(remainList[i] != 0) {
				answer++;
			}
		}
		
		//결과 출력
		System.out.println(answer);
	}
}
