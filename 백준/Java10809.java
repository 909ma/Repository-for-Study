/*
 * @Author : 909ma
 * 
 * @Date : 2023. 5. 19
 * 
 * @Function :
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java10809 {
    public static void main(String[] agrs) {
	Scanner scanner = new Scanner(System.in);
	String inputString = scanner.nextLine();
	scanner.close();

	//문자열 정보 담을 리스트
	int[] numberList = new int[26];
	Arrays.fill(numberList, -1);
	
	for(int i = 0; i < inputString.length() ; i++) {
		int stringNumber = Character.getNumericValue(inputString.charAt(i))-10;
		if(numberList[stringNumber]==-1) {
		numberList[stringNumber]=i;
		}
	}
	
	for(int i = 0; i < 26; i++) {
		System.out.printf("%d ",numberList[i]);
	}
	// a는 10임, z는 35
    }
}
