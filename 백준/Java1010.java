/*
	@Author   : 909ma
	@Date     : 2023. 5. 26
	@Function : 
 */
package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;

public class Java1010 {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	int testCase = Integer.parseInt(br.readLine());
	StringBuilder sb = new StringBuilder();
	for (int i = 0; i < testCase; i++) {
	    String[] line = br.readLine().split(" ");
	    int N = Integer.parseInt(line[0]);
	    int M = Integer.parseInt(line[1]);
	    BigInteger answer = factorial(M).divide(factorial(N).multiply(factorial(M - N)));
	    sb.append(answer).append("\n");
	}
	bw.write(sb + "\n");
	bw.flush();
	bw.close();
	br.close();
    }

    public static BigInteger factorial(int n) {
	BigInteger result = BigInteger.ONE;
	for (int i = 2; i <= n; i++) {
	    result = result.multiply(BigInteger.valueOf(i));
	}
	return result;
    }
}
