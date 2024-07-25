/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java27323 {
    public static void main(String[] args) {
	boolean errorChecker = false;
	Scanner scanner = new Scanner(System.in);
	int A = scanner.nextInt();
	int B = scanner.nextInt();
	scanner.close();
	// 예외처리
	if (A < 1 || A > 100) {
	    System.out.println("ERROR A");
	    errorChecker = true;
	}
	if (B < 1 || B > 100) {
	    System.out.println("ERROR B");
	    errorChecker = true;
	}
	if (errorChecker) {
	    return;
	}
	System.out.println(A * B);
    }
}
