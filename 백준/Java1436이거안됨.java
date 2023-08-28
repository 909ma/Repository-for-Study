/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java1436이거안됨 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	scanner.close();
	if (N < 1 || N > 10000) {
	    System.out.println("ERROR N");
	    return;
	}

	int count = 0;
	int answer = 0;
	for (int i = 666; count != N; i++) {
	    String string = Integer.toString(i);
	    int length = string.length();
	    for (int j = 0; j < length - 3; j++) {
		if (string.charAt(j) == '6' && string.charAt(j + 1) == '6' && string.charAt(j + 2) == '6') {
		    count++;
		    answer = i;
		}
		System.out.println("안쪽 도는 중");
	    }
	    System.out.println("바깥 쪽 도는 중 : " + i);

	}

	System.out.println(answer);
    }
}
