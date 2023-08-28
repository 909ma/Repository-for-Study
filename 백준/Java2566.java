/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2566 {
    public static void main(String[] args) {
	final int X = 9;
	final int Y = 9;
	final int MAX_OF_NUMBER = 100;
	int[][] Matrix = new int[X][Y];
	Scanner scanner = new Scanner(System.in);
	for (int i = 0; i < X; i++) {
	    String[] line = scanner.nextLine().split(" ");
	    for (int j = 0; j < Y; j++) {
		Matrix[i][j] = Integer.parseInt(line[j]);
		if (Matrix[i][j] > MAX_OF_NUMBER || Matrix[i][j] < 0) {
		    System.out.println("ERROR");
		    scanner.close();
		    return;
		}
	    }
	}
	scanner.close();
	int Max = 0;
	int indexX = 0, indexY = 0;
	for (int i = 0; i < X; i++) {
	    for (int j = 0; j < Y; j++) {
		if (Matrix[i][j] >= Max) {
		    Max = Matrix[i][j];
		    indexX = i + 1;
		    indexY = j + 1;
		}
	    }
	}
	System.out.println(Max);
	System.out.printf("%d %d\n", indexX, indexY);
    }
}
