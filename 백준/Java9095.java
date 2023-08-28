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

public class Java9095 {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	StringBuilder sb = new StringBuilder();

	int testCase = Integer.parseInt(br.readLine());
	for (int now = 0; now < testCase; now++) {
	    int number = Integer.parseInt(br.readLine());
	    int count3 = number / 3;
	    int count2 = number / 2;
	    int count1 = number;
	    int count = 0;

	    for (int i = 0; i <= count3; i++) {
		for (int j = 0; j <= count2; j++) {
		    for (int k = 0; k <= count1; k++) {
			if (i * 3 + j * 2 + k * 1 == number) {
			    count += factorial(i + j + k) / (factorial(i) * factorial(j) * factorial(k));
			}
		    }
		}
	    }

	    sb.append(count).append("\n");
	}

	bw.append(sb.toString());
	bw.flush();
	bw.close();
	br.close();
    }

    public static int factorial(int number) {
	int sum = 1;
	for (int i = number; i > 0; i--) {
	    sum *= i;
	}
	return sum;
    }
}
