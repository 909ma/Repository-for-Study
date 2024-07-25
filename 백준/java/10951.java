/*
	@Author   : 909ma
	@Date     : 2023. 5. 25
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10951 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);

	while (scanner.hasNextInt()) {
	    int a = scanner.nextInt();
	    int b = scanner.nextInt();
	    int sum = a + b;
	    System.out.println(sum);
	}
	scanner.close();
    }
}
