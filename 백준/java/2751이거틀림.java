/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java2751이거틀림 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	int[] list = new int[N];
	for (int i = 0; i < N; i++) {
	    list[i] = scanner.nextInt();
	}
	scanner.close();

	Arrays.sort(list);

	for (int i = 0; i < N; i++) {
	    System.out.println(list[i]);
	}
    }
}
