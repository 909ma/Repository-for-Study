/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2738 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int x = scanner.nextInt();
	int y = scanner.nextInt();
	if (x < 1 || y < 1) {
	    System.out.println("ERROR");
	    scanner.close();
	    return;
	}
	int[][] Matrix1 = new int[x][y];
	int[][] Matrix2 = new int[x][y];
	int[][] sum = new int[x][y];
	for (int i = 0; i < x; i++) {
	    for (int j = 0; j < y; j++) {
		Matrix1[i][j] = scanner.nextInt();
	    }
	}
	for (int i = 0; i < x; i++) {
	    for (int j = 0; j < y; j++) {
		Matrix2[i][j] = scanner.nextInt();
	    }
	}
	scanner.close();

	for (int i = 0; i < x; i++) {
	    for (int j = 0; j < y; j++) {
		sum[i][j] = Matrix1[i][j] + Matrix2[i][j];
		System.out.printf("%d ", sum[i][j]);
	    }
	    System.out.println();
	}
    }
}
