/*
 * @Author : 909ma
 * 
 * @Date : 2023. 5. 24
 * 
 * @Function :
 */

package practice;

import java.util.Scanner;

public class Java11047 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	int k = scanner.nextInt();
	int[] list = new int[N];
	for (int i = 0; i < N; i++) {
	    list[i] = scanner.nextInt();
	}
	scanner.close();

	int count = 0;
	int length = list.length;
	for (int i = length - 1; i >= 0; i--) {
	    if (list[i] > k) {
		continue;
	    } else {
		count += k / list[i];
		k %= list[i];
	    }

	}

	System.out.println(count);
    }
}
