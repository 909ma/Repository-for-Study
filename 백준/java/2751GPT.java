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

public class Java2751GPT {
    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int N = Integer.parseInt(br.readLine());

	int[] numbers = new int[N];
	for (int i = 0; i < N; i++) {
	    numbers[i] = Integer.parseInt(br.readLine());
	}

	Arrays.sort(numbers);

	StringBuilder sb = new StringBuilder();
	for (int i = 0; i < N; i++) {
	    sb.append(numbers[i]).append('\n');
	}

	System.out.println(sb.toString());
    }
}
