/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10813GPT {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberSize = scanner.nextInt();
        if (!checkRange(numberSize, 1, 100)) {
            System.out.println("ERROR: numberSize is out of range");
            scanner.close();
            return;
        }

        int tryTimes = scanner.nextInt();
        if (!checkRange(tryTimes, 1, 100)) {
            System.out.println("ERROR: tryTimes is out of range");
            scanner.close();
            return;
        }

        int[] numberCup = new int[numberSize];
        for (int i = 0; i < numberSize; i++) {
            numberCup[i] = i + 1;
        }

        for (int i = 0; i < tryTimes; i++) {
            int startNumber = scanner.nextInt();
            if (!checkRange(startNumber, 1, numberSize)) {
                System.out.println("ERROR: startNumber is out of range");
                scanner.close();
                return;
            }

            int endNumber = scanner.nextInt();
            if (!checkRange(endNumber, startNumber, numberSize)) {
                System.out.println("ERROR: endNumber is out of range");
                scanner.close();
                return;
            }

            int temp = numberCup[startNumber - 1];
            numberCup[startNumber - 1] = numberCup[endNumber - 1];
            numberCup[endNumber - 1] = temp;
        }
        scanner.close();

        for (int i = 0; i < numberSize; i++) {
            System.out.print(numberCup[i] + " ");
        }
    }

    private static boolean checkRange(int value, int minValue, int maxValue) {
        return value >= minValue && value <= maxValue;
    }
}
