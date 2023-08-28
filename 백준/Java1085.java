/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1085 {

    public static void main(String[] args) {
	boolean error = false;
	Scanner scanner = new Scanner(System.in);
	int x = scanner.nextInt();
	int y = scanner.nextInt();
	int w = scanner.nextInt();
	int h = scanner.nextInt();
	scanner.close();

	if (x < 1 || x > w - 1) {
	    System.out.println("ERROR x");
	    error = true;
	}
	if (y < 1 || y > h - 1) {
	    System.out.println("ERROR y");
	    error = true;
	}
	if (w < 1 || w > 1000) {
	    System.out.println("ERROR w");
	    error = true;
	}
	if (h < 1 || h > 1000) {
	    System.out.println("ERROR h");
	    error = true;
	}
	if (error) {
	    return;
	}

	int a = w - x;
	if (a > x) {
	    a = x;
	}
	int b = h - y;
	if (b > y) {
	    b = y;
	}
	if (a >= b) {
	    System.out.println(b);
	} else {
	    System.out.println(a);
	}
    }
}
