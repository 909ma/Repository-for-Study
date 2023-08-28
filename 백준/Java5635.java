package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Java5635 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int testCase = Integer.parseInt(br.readLine());
		String[] name = new String[testCase];
		int[] birth = new int[testCase];
		for(int i = 0; i<testCase; i++) {
			String[] input = br.readLine().split(" ");
			

			name[i] = input[0];
			int days = Integer.parseInt(input[1]);
			int month = Integer.parseInt(input[2]);
			int year = Integer.parseInt(input[3]);
			birth[i] = 100000 * year + 1000 * month + days;
		}
		int max = Arrays.stream(birth).max().getAsInt();
		int min = Arrays.stream(birth).min().getAsInt();
		int maxIndex=0, minIndex=0;
		for(int i = 0; i < testCase; i++) {
			if(max == birth[i]) {
				maxIndex=i;
			}
			if(min == birth[i]) {
				minIndex=i;
			}
		}
		sb.append(name[maxIndex]).append("\n").append(name[minIndex]);
		
		bw.write(sb + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}
