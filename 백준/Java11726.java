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

public class Java11726 {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	int n = Integer.parseInt(br.readLine());
	BigInteger answer = BigInteger.ZERO;
	int max2 = n / 2;
	for (int i = 0; i <= max2; i++) {
	    int factor = n - 2 * i;
	    BigInteger binomialCoefficient = factorial(i + factor).divide(factorial(i).multiply(factorial(factor)));
	    answer = answer.add(binomialCoefficient);
	}
	answer = answer.mod(BigInteger.valueOf(10007));

	bw.write(answer.toString() + "\n");

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