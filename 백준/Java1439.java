package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Java1439 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        int length = input.length();
        int count = 0;

        char prevChar = input.charAt(0);
        for (int i = 1; i < length; i++) {
            char currChar = input.charAt(i);
            if (prevChar != currChar) {
                count++;
            }
            prevChar = currChar;
        }

        bw.write(String.valueOf((count + 1) / 2));
        bw.flush();
        bw.close();
        br.close();
    }
}
