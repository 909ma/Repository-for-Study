/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java8393GPT {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();

        try {
            if (number > 10000 || number < 1) {
                throw new IllegalArgumentException("ERROR n");
            }

            int answer = 0;
            for (int i = 1; i <= number; i++) {
                answer += i;
            }
            System.out.println(answer);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
