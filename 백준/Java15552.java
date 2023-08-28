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

public class Java15552 {
    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	int count = Integer.parseInt(br.readLine());

	for (int i = 0; i < count; i++) {
	    String[] input = br.readLine().split(" ");
	    int a = Integer.parseInt(input[0]);
	    int b = Integer.parseInt(input[1]);
	    int sum = a + b;
	    bw.write(sum + "\n");
	}

	bw.flush();
	bw.close();
	br.close();
    }
}
