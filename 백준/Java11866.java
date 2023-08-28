package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class Java11866 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		String[] line = br.readLine().split(" ");
		int N = Integer.parseInt(line[0]);
		int K = Integer.parseInt(line[1]);
		Queue<Integer> queue = new LinkedList<>();
		for(int i = 1; i <= N; i++) {
			queue.add(i);
		}
		sb.append("<");
		boolean isNotFirst = false;
		while(queue.peek() != null) {
			if(isNotFirst) {
				sb.append(", ");
			}
			for(int i = 0; i < K-1; i++) {
				int a = queue.remove();
				queue.add(a);
			}
			int b = queue.remove();
			sb.append(b);
			if(!(isNotFirst)) {
				isNotFirst = true;
			}
		}
		bw.write(sb + ">");
		
		bw.flush();
		bw.close();
		br.close();
	}
}
