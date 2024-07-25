/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1010시간초과 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int count = scanner.nextInt();
	StringBuilder sb = new StringBuilder();
	for (int i = 0; i < count; i++) {
	    int a = scanner.nextInt();
	    int b = scanner.nextInt();
	    int answer = 1;
	    for (int j = b; b > (b - a); b--) {
		answer *= j;
	    }
	    sb.append(answer).append("\n");
	}
	scanner.close();

	System.out.println(sb);
    }

}
