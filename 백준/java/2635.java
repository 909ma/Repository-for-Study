package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Java2635 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int number = Integer.parseInt(br.readLine());
        ArrayList<Integer> sequence = new ArrayList<>();

        int index = 0;
        int max = 0;
        int num1, num2, temp;

        for (int i = number; i > 0; i--) {
            ArrayList<Integer> tempSequence = new ArrayList<>();
            tempSequence.add(number);
            tempSequence.add(i);

            while (true) {
                temp = tempSequence.get(tempSequence.size() - 2) - tempSequence.get(tempSequence.size() - 1);
                if (temp < 0) {
                    break;
                }
                tempSequence.add(temp);
            }

            if (tempSequence.size() > max) {
                index = i;
                max = tempSequence.size();
                sequence = tempSequence;
            }
        }

        sb.append(max).append("\n");
        for (int i = 0; i < sequence.size(); i++) {
            sb.append(sequence.get(i));
            if (i != sequence.size() - 1) {
                sb.append(" ");
            }
        }

        bw.write(sb.toString() + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

