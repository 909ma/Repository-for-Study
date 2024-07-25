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
import java.util.Arrays;

public class Java1920 {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	int N = Integer.parseInt(br.readLine());
	int[] listN = new int[N];
	String[] line = br.readLine().split(" ");
	for (int i = 0; i < N; i++) {
	    listN[i] = Integer.parseInt(line[i]);
	}
	int M = Integer.parseInt(br.readLine());
	int[] listM = new int[M];
	line = br.readLine().split(" ");
	for (int i = 0; i < M; i++) {
	    listM[i] = Integer.parseInt(line[i]);
	}
	boolean[] exist = new boolean[M];
	Arrays.fill(exist, false);
	Arrays.sort(listN);

	for (int i = 0; i < M; i++) {
	    for (int j = 0; j < N; j++) {
		if (listM[i] == listN[j]) {
		    exist[i] = true;
		    break;
		}
	    }
	}

	for (int i = 0; i < M; i++) {
	    if (exist[i]) {
		bw.write(1 + "\n");
	    } else {
		bw.write(0 + "\n");
	    }
	}

	bw.flush();
	bw.close();
	br.close();
    }
}
