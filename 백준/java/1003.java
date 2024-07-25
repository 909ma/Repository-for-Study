/*
	@Author   : 909ma
	@Date     : 2023. 5. 25
	@Function : 
 */
package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Java1003 {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	int testCase = Integer.parseInt(br.readLine());
	int[] testNumber = new int[testCase];
	int max = 1;
	for (int i = 0; i < testCase; i++) {
	    testNumber[i] = Integer.parseInt(br.readLine());
	    if (max < testNumber[i]) {
		max = testNumber[i];
	    }
	}

	int[][] fibonacci = new int[max + 1][2];
	fibonacci[0][0] = 0;
	fibonacci[0][1] = 1;
	fibonacci[1][0] = 1;
	fibonacci[1][1] = 0;
	for (int i = 2; i <= max; i++) {
	    fibonacci[i][0] = fibonacci[i - 1][0] + fibonacci[i - 2][0];
	    fibonacci[i][1] = fibonacci[i - 1][1] + fibonacci[i - 2][1];
	}

	for (int i = 0; i < testCase; i++) {
	    System.out.printf("%d %d\n", fibonacci[testNumber[i]][1], fibonacci[testNumber[i]][0]);
	}
	bw.flush();
	bw.close();
	br.close();
    }
}
