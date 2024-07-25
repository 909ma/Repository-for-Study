package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Java15904 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String line = br.readLine();

		boolean check1 = false, check2 = false, check3 = false, check4 = false;
		for (int i = 0; i < line.length(); i++) {
			char c = line.charAt(i);
			if (check1 == false) {
				if (c == 'U') {
					check1 = true;
				}
			}
			else if (check2 == false) {
				if (c == 'C') {
					check2 = true;
				}
			}
			else if (check3 == false) {
				if (c == 'P') {
					check3 = true;
				}
			}
			else if (check4 == false) {
				if (c == 'C') {
					check4 = true;
					break;
				}
			}
		}
		if (check1 & check2 & check3 & check4) {
			bw.write("I love UCPC");
		}
		else {
			bw.write("I hate UCPC");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
