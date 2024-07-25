/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java9063 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int positionCase = scanner.nextInt();
	int[][] position = new int[positionCase][2];
	for (int i = 0; i < positionCase; i++) {
	    position[i][0] = scanner.nextInt();
	    position[i][1] = scanner.nextInt();
	}
	scanner.close();

	int min = position[0][0], max = position[0][0];
	for (int i = 0; i < positionCase; i++) {
	    if (min > position[i][0]) {
		min = position[i][0];
	    }
	    if (max < position[i][0]) {
		max = position[i][0];
	    }
	}
	int x = max - min;
	min = position[0][1];
	max = position[0][1];
	for (int i = 0; i < positionCase; i++) {
	    if (min > position[i][1]) {
		min = position[i][1];
	    }
	    if (max < position[i][1]) {
		max = position[i][1];
	    }
	}
	int y = max - min;

	System.out.println(x * y);
    }
}
