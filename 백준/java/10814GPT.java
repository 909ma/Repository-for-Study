/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10814GPT {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int count = Integer.parseInt(scanner.nextLine());
	Member[] members = new Member[count];

	for (int i = 0; i < count; i++) {
	    String[] line = scanner.nextLine().split(" ");
	    int age = Integer.parseInt(line[0]);
	    String name = line[1];
	    members[i] = new Member(age, name);
	}
	scanner.close();

	mergeSort(members, 0, count - 1);

	for (Member member : members) {
	    System.out.printf("%d %s\n", member.getAge(), member.getName());
	}
    }

    static class Member {
	private int age;
	private String name;

	public Member(int age, String name) {
	    this.age = age;
	    this.name = name;
	}

	public int getAge() {
	    return age;
	}

	public String getName() {
	    return name;
	}
    }

    static void mergeSort(Member[] members, int left, int right) {
	if (left < right) {
	    int mid = (left + right) / 2;
	    mergeSort(members, left, mid);
	    mergeSort(members, mid + 1, right);
	    merge(members, left, mid, right);
	}
    }

    static void merge(Member[] members, int left, int mid, int right) {
	int n1 = mid - left + 1;
	int n2 = right - mid;

	Member[] L = new Member[n1];
	Member[] R = new Member[n2];

	for (int i = 0; i < n1; i++) {
	    L[i] = members[left + i];
	}
	for (int j = 0; j < n2; j++) {
	    R[j] = members[mid + 1 + j];
	}

	int i = 0, j = 0;
	int k = left;

	while (i < n1 && j < n2) {
	    if (L[i].getAge() <= R[j].getAge()) {
		members[k] = L[i];
		i++;
	    } else {
		members[k] = R[j];
		j++;
	    }
	    k++;
	}

	while (i < n1) {
	    members[k] = L[i];
	    i++;
	    k++;
	}

	while (j < n2) {
	    members[k] = R[j];
	    j++;
	    k++;
	}
    }
}
