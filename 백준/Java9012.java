/*
 * @Author : 909ma
 * 
 * @Date : 2023. 5. 24
 * 
 * @Function :
 */

package practice;

import java.util.Scanner;

public class Java9012 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int count = Integer.parseInt(scanner.nextLine());
		String[] input = new String[count];
		for(int i = 0; i < count; i++) {
			input[i] = scanner.nextLine();
		}
		scanner.close();
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < count; i++) {
            int parenCount = 0; // 괄호 개수 추적 변수
            boolean check = true;
            int length = input[i].length();
            for (int j = 0; j < length; j++) {
                if (input[i].charAt(j) == '(') {
                    parenCount++;
                } else if (input[i].charAt(j) == ')') {
                    parenCount--;
                }
                if (parenCount < 0) {
                    check = false;
                    break;
                }
            }
            if (check && parenCount == 0) {
                sb.append("YES\n");
            } else {
                sb.append("NO\n");
            }
        }
		
		System.out.println(sb);
	}
}
