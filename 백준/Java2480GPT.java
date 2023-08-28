/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java2480GPT {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] dice = new int[3];

        for (int i = 0; i < 3; i++) {
            int value = scanner.nextInt();
            if (value < 1 || value > 6) {
                System.out.println("ERROR");
                scanner.close();
                return;
            }
            dice[i] = value;
        }

        scanner.close();

        int prize = calculatePrize(dice);
        System.out.println(prize);
    }

    public static int calculatePrize(int[] dice) {
        int[] count = new int[7]; // 주사위 눈의 개수를 세기 위한 배열

        // 주사위 눈의 개수 세기
        for (int i = 0; i < dice.length; i++) {
            count[dice[i]]++;
        }

        int maxCount = 0; // 가장 많이 나온 눈의 개수
        int maxNum = 0; // 가장 많이 나온 눈의 값

        // 가장 많이 나온 눈과 그 개수 찾기
        for (int i = 1; i <= 6; i++) {
            if (count[i] > maxCount) {
                maxCount = count[i];
                maxNum = i;
            }
        }

        int prize = 0; // 상금 초기화

        if (maxCount == 3) { // 같은 눈이 3개 나온 경우
            prize = 10000 + maxNum * 1000;
        } else if (maxCount == 2) { // 같은 눈이 2개 나온 경우
            prize = 1000 + maxNum * 100;
        } else { // 모두 다른 눈이 나온 경우
            for (int i = 0; i < dice.length; i++) {
                if (dice[i] > maxNum) {
                    maxNum = dice[i];
                }
            }
            prize = maxNum * 100;
        }

        return prize;
    }
}
