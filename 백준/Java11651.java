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
import java.util.Comparator;

public class Java11651 {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	int testCase = Integer.parseInt(br.readLine());
	int[][] list = new int[testCase][2];
	for (int i = 0; i < testCase; i++) {
	    String[] line = br.readLine().split(" ");
	    list[i][0] = Integer.parseInt(line[0]);
	    list[i][1] = Integer.parseInt(line[1]);
	}

	Arrays.sort(list, new Comparator<int[]>() {
	    @Override
	    public int compare(int[] o1, int[] o2) {
		// y좌표를 우선으로 오름차순 정렬하고, y좌표가 같은 경우 x좌표를 오름차순 정렬합니다.
		if (o1[1] == o2[1]) {
		    return Integer.compare(o1[0], o2[0]);
		} else {
		    return Integer.compare(o1[1], o2[1]);
		}
	    }
	});

	StringBuilder sb = new StringBuilder();
	for (int i = 0; i < testCase; i++) {
	    sb.append(list[i][0]).append(" ").append(list[i][1]).append("\n");
	}

	bw.write(sb.toString());
	bw.flush();
	bw.close();
	br.close();
    }
}
