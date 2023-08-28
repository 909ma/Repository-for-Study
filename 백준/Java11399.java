/*
 * @Author : 909ma
 * 
 * @Date : 2023. 5. 24
 * 
 * @Function :
 */

package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java11399 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int[] people = new int[N];
		for(int i = 0; i < N ; i++) {
			people[i] = scanner.nextInt();
		}
		scanner.close();
		
		Arrays.sort(people);
		int sum = 0;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j <= i; j++) {
				sum += people[j];
			}
		}
		System.out.println(sum);
	}
}
