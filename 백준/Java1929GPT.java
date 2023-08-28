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

public class Java1929GPT {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	String[] input = br.readLine().split(" ");
	int M = Integer.parseInt(input[0]);
	int N = Integer.parseInt(input[1]);

	boolean[] isPrime = new boolean[N + 1];
	for (int i = 2; i <= N; i++) {
	    isPrime[i] = true;
	}

	for (int i = 2; i * i <= N; i++) {
	    if (isPrime[i]) {
		for (int j = i * i; j <= N; j += i) {
		    isPrime[j] = false;
		}
	    }
	}

	StringBuilder sb = new StringBuilder();
	for (int i = M; i <= N; i++) {
	    if (isPrime[i]) {
		sb.append(i).append("\n");
	    }
	}
	bw.append(sb.toString());

	bw.flush();
	bw.close();
	br.close();
    }
}
