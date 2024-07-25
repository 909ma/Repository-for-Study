/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Java10989GPT {
    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int N = Integer.parseInt(br.readLine()); // 입력값의 개수
	int[] count = new int[10001]; // 입력값의 범위는 1부터 10,000까지

	// 입력값의 개수를 카운팅하여 저장합니다.
	for (int i = 0; i < N; i++) {
	    int num = Integer.parseInt(br.readLine());
	    count[num]++;
	}

	// 카운트 배열을 순회하면서 해당 숫자의 개수만큼 출력합니다.
	StringBuilder sb = new StringBuilder();
	for (int i = 1; i <= 10000; i++) {
	    while (count[i] > 0) {
		sb.append(i).append('\n');
		count[i]--;
	    }
	}

	System.out.println(sb.toString());
    }
}
