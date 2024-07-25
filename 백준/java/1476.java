package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Java1476 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] line = br.readLine().split(" ");
		int E = Integer.parseInt(line[0]);
		int S = Integer.parseInt(line[1]);
		int M = Integer.parseInt(line[2]);
		
		int year = 1;
		while(true) {
			if(E*S*M==1) {
				break;
			}
			E--;
			S--;
			M--;
			if(E==0) {
				E=15;
			}
			if(S==0) {
				S=28;
			}
			if(M==0) {
				M=19;
			}
			year++;
		}
		bw.write(year + "\n");
		
		
		bw.flush();
		bw.close();
		br.close();
	}
}
