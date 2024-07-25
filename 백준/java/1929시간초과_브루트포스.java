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

public class Java1929시간초과_브루트포스 {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	String[] input = br.readLine().split(" ");
	int M = Integer.parseInt(input[0]);
	int N = Integer.parseInt(input[1]);

	StringBuilder sb = new StringBuilder();
	for (int i = M; i <= N; i++) {
	    boolean check = true;
	    for (int j = 2; j < i; j++) {
		if (i % j == 0) {
		    check = false;
		    break;
		}
	    }
	    if (check) {
		sb.append(i).append("\n");
	    }
	}
	bw.append(sb.toString());

	bw.flush();
	bw.close();
	br.close();
    }
}
