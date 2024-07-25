/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Arrays;
import java.util.Scanner;

public class Java10989이거안됨 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	int[] array = new int[N];
	for (int i = 0; i < N; i++) {
	    array[i] = scanner.nextInt();
	}
	scanner.close();

	countingSort(array);

	for (int i = 0; i < N; i++) {
	    System.out.println(array[i]);
	}
    }

    public static void countingSort(int[] array) {
	// 입력 배열의 최댓값을 구합니다.
	int max = Arrays.stream(array).max().getAsInt();

	// 카운트 배열을 생성하고 각 원소의 개수를 세어 저장합니다.
	int[] count = new int[max + 1];
	for (int num : array) {
	    count[num]++;
	}

	// 누적 합을 계산합니다.
	for (int i = 1; i <= max; i++) {
	    count[i] += count[i - 1];
	}

	// 정렬된 결과를 저장할 배열을 생성합니다.
	int[] sortedArray = new int[array.length];

	// 입력 배열을 뒤에서부터 순회하면서 정렬된 위치에 원소를 배치합니다.
	for (int i = array.length - 1; i >= 0; i--) {
	    int num = array[i];
	    sortedArray[count[num] - 1] = num;
	    count[num]--;
	}

	// 정렬된 결과를 원래 배열에 복사합니다.
	System.arraycopy(sortedArray, 0, array, 0, array.length);
    }
}
