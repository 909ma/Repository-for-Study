/*
 * @Author : 909ma
 * 
 * @Date : 2023. 5. 24
 * 
 * @Function :
 */
package practice;

import java.util.Scanner;

public class Java1065 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();

        int count = 0;
        for (int i = 1; i <= N; i++) {
            if (isHanNumber(i)) {
                count++;
            }
        }

        System.out.println(count);
    }

    private static boolean isHanNumber(int number) {
        if (number < 100) {
            return true;
        }

        int digit1 = number / 100; // 백의 자리 숫자
        int digit2 = (number % 100) / 10; // 십의 자리 숫자
        int digit3 = number % 10; // 일의 자리 숫자

        if ((digit2 * 2) == (digit1 + digit3)) {
            return true;
        }

        return false;
    }
}
