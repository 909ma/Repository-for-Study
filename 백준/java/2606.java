/*
	@Author   : 909ma
	@Date     : 2023. 5. 25
	@Function : 
 */
package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class Java2606 {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	int numberOfComputer = Integer.parseInt(br.readLine());
	int testCase = Integer.parseInt(br.readLine());
	int[][] computerRelations = new int[numberOfComputer + 1][numberOfComputer + 1];

	for (int i = 0; i < testCase; i++) {
	    String[] line = br.readLine().split(" ");
	    int a = Integer.parseInt(line[0]);
	    int b = Integer.parseInt(line[1]);
	    computerRelations[a][b] = 1;
	    computerRelations[b][a] = 1;
	}

	int count = countVirus(computerRelations, 1);
	// System.out.println(count - 1);
	bw.write(--count + "\n");

	bw.flush();
	bw.close();
	br.close();
    }

    public static int countVirus(int[][] computerRelations, int start) {
	int count = 0; // 바이러스에 감염된 컴퓨터의 수를 저장하는 변수
	boolean[] visited = new boolean[computerRelations.length]; // 각 컴퓨터의 방문 여부를 저장하는 배열
	Queue<Integer> queue = new LinkedList<>(); // 큐 생성
	queue.add(start); // 시작 컴퓨터를 큐에 추가
	visited[start] = true; // 시작 컴퓨터를 방문 처리

	while (!queue.isEmpty()) { // 큐가 비어있지 않은 동안 반복
	    int current = queue.poll(); // 큐의 맨 앞에 있는 컴퓨터를 꺼냄
	    count++; // 바이러스에 감염된 컴퓨터의 수 증가

	    for (int i = 1; i < computerRelations.length; i++) {
		// 현재 컴퓨터와 연결된 컴퓨터 중에서 아직 방문하지 않은 컴퓨터를 큐에 추가하고 방문 처리
		if (computerRelations[current][i] == 1 && !visited[i]) {
		    queue.add(i);
		    visited[i] = true;
		}
	    }
	}

	return count; // 바이러스에 감염된 컴퓨터의 수 반환
    }
}
