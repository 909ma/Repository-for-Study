/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10950GPT {
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int max = scanner.nextInt();
        int[] answer = new int[max];

        StringBuilder sb = new StringBuilder(); // StringBuilder 추가

        for (int i = 0; i < max; i++) {
            int a = scanner.nextInt();
            if (a <= 0) {
                System.out.println("ERROR A");
                scanner.close();
                return;
            }
            int b = scanner.nextInt();
            if (b >= 10) {
                System.out.println("ERROR B");
                scanner.close();
                return;
            }
            answer[i] = a + b;
            sb.append(answer[i]).append("\n"); // 결과를 StringBuilder에 추가
        }
        scanner.close();

        System.out.print(sb); // StringBuilder 출력
    }
}
