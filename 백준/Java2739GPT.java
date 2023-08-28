/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2739GPT {
	public static final int MIN_NUMBER = 1;
    public static final int MAX_NUMBER = 9;

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int number = scanner.nextInt();
            if (number < MIN_NUMBER || number > MAX_NUMBER) {
                System.out.println("ERROR");
                return;
            }

            StringBuilder sb = new StringBuilder();
            for (int i = 1; i <= MAX_NUMBER; i++) {
                sb.append(number).append(" * ").append(i).append(" = ").append(number * i).append("\n");
            }
            System.out.print(sb);
        }
    }
}
