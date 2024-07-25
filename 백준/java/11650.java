/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Java11650 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int count = scanner.nextInt();
	int[][] position = new int[count][2];
	for (int i = 0; i < count; i++) {
	    position[i][0] = scanner.nextInt();
	    position[i][1] = scanner.nextInt();
	}
	scanner.close();
	Arrays.sort(position, new Comparator<int[]>() {
	    @Override
	    public int compare(int[] a, int[] b) {
		if (a[0] == b[0]) {
		    return Integer.compare(a[1], b[1]); // 첫 번째 열 값이 같은 경우 두 번째 열 값으로 비교
		} else {
		    return Integer.compare(a[0], b[0]); // 첫 번째 열 값으로 비교
		}
	    }
	});
	for (int i = 0; i < count; i++) {
	    System.out.printf("%d %d\n", position[i][0], position[i][1]);
	}
    }
}
