/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java19532 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int a = scanner.nextInt();
	int b = scanner.nextInt();
	int c = scanner.nextInt();
	int d = scanner.nextInt();
	int e = scanner.nextInt();
	int f = scanner.nextInt();
	scanner.close();

	int x = 0, y = 0;

	for (int i = -999; i <= 999; i++) {
	    for (int j = -999; j <= 999; j++) {
		if (a * i + b * j == c) {
		    if (d * i + e * j == f) {
			x = i;
			y = j;
			break;
		    }
		}
	    }
	}

	System.out.printf("%d %d", x, y);
    }
}
