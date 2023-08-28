/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1546 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		//시험 과목 수 입력
		int number = scanner.nextInt();
		if(number < 0 || number > 1000) {
			System.out.println("ERROR");
			scanner.close();
			return;
		}
		
		//성적 입력
		int[] point = new int[number];
		int sum = 0;
		for(int i = 0; i < number; i++) {
			point[i] = scanner.nextInt();
			if(point[i] > 100 || point[i] < 0) {
				System.out.println("ERROR");
				scanner.close();
				return;
			}
			sum += point[i];
		}
		if(sum == 0) {
			System.out.println("ERROR");
			scanner.close();
			return;
		}
		scanner.close();
		
		//새로운 평균 구하기
		int max = point[0];
		int sum1 = 0;
		for(int i = 0; i < number ; i++) {
			if(max < point[i]) {
				max = point[i];
			}
			sum1 += point[i];
		}
		
		//출력
		double avg = (double)sum1/number*100/max;
		System.out.println(avg);
	}
}
