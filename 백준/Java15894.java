/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java15894 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	long n = scanner.nextLong();
	scanner.close();
	if (n < 1 || n > 1000000000) {
	    System.out.println("ERROR n");
	    return;
	}
	long area = 4 * n;
	System.out.println(area);
    }
}
