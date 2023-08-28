/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Java1181GPT {
    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int N = Integer.parseInt(br.readLine()); // 단어의 개수

	String[] words = new String[N]; // 단어 배열

	for (int i = 0; i < N; i++) {
	    words[i] = br.readLine();
	}

	Arrays.sort(words, new Comparator<String>() {
	    @Override
	    public int compare(String o1, String o2) {
		if (o1.length() == o2.length()) {
		    return o1.compareTo(o2); // 길이가 같은 경우 사전순으로 정렬
		} else {
		    return o1.length() - o2.length(); // 길이가 다른 경우 길이가 짧은 순으로 정렬
		}
	    }
	});

	StringBuilder sb = new StringBuilder();
	for (String word : words) {
	    sb.append(word).append('\n');
	}

	System.out.println(sb.toString());
    }
}
