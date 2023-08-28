/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Java10815GPT {
    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int N = Integer.parseInt(br.readLine()); // 숫자 카드의 개수
	int[] cards = new int[N]; // 숫자 카드 배열

	StringTokenizer st = new StringTokenizer(br.readLine());
	for (int i = 0; i < N; i++) {
	    cards[i] = Integer.parseInt(st.nextToken());
	}

	Arrays.sort(cards); // 이진 탐색을 위해 배열을 정렬합니다.

	int M = Integer.parseInt(br.readLine()); // 찾을 숫자의 개수

	StringBuilder sb = new StringBuilder();
	st = new StringTokenizer(br.readLine());
	for (int i = 0; i < M; i++) {
	    int target = Integer.parseInt(st.nextToken());

	    if (binarySearch(cards, target)) {
		sb.append("1 ");
	    } else {
		sb.append("0 ");
	    }
	}

	System.out.println(sb.toString());
    }

    private static boolean binarySearch(int[] arr, int target) {
	int start = 0;
	int end = arr.length - 1;

	while (start <= end) {
	    int mid = (start + end) / 2;

	    if (arr[mid] == target) {
		return true; // 숫자를 찾았을 경우 true를 반환합니다.
	    } else if (arr[mid] < target) {
		start = mid + 1; // 중간 값보다 큰 경우 오른쪽 절반을 탐색합니다.
	    } else {
		end = mid - 1; // 중간 값보다 작은 경우 왼쪽 절반을 탐색합니다.
	    }
	}

	return false; // 숫자를 찾지 못한 경우 false를 반환합니다.
    }
}
