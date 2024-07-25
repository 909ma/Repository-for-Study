package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Java1769 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String input = br.readLine();

		int count = 0;
		while (input.length() > 1) {
			int sum = 0;
			for (int i = 0; i < input.length(); i++) {
				sum += input.charAt(i) - '0';
			}
			input = String.valueOf(sum);
			count++;
		}

		bw.write(count + "\n");
		if (input.equals("3") || input.equals("6") || input.equals("9")) {
			bw.write("YES");
		}
		else {
			bw.write("NO");
		}

		bw.flush();
		bw.close();
		br.close();
	}
}
