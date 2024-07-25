/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java3009 {

    public static void main(String[] args) {
	int[][] position = new int[4][2];
	Scanner scanner = new Scanner(System.in);
	position[0][0] = scanner.nextInt();
	position[0][1] = scanner.nextInt();
	position[1][0] = scanner.nextInt();
	position[1][1] = scanner.nextInt();
	position[2][0] = scanner.nextInt();
	position[2][1] = scanner.nextInt();
	scanner.close();

	int x1 = position[0][0], x2 = position[1][0], x3 = position[2][0];
	if (x1 == x2) {
	    position[3][0] = x3;
	} else if (x1 == x3) {
	    position[3][0] = x2;
	} else {
	    position[3][0] = x1;
	}

	int y1 = position[0][1], y2 = position[1][1], y3 = position[2][1];
	if (y1 == y2) {
	    position[3][1] = y3;
	} else if (y1 == y3) {
	    position[3][1] = y2;
	} else {
	    position[3][1] = y1;
	}

	System.out.printf("%d %d", position[3][0], position[3][1]);
    }
}
