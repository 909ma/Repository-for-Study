/*
	@Author   : 909ma
	@Date     : 2023. 5. 24
	@Function : 
 */
package practice;

import java.util.Arrays;

public class Java4673 {

    public static void main(String[] args) {
	int[] list = new int[10000];
	Arrays.fill(list, 0);
	for (int i = 1; i <= 10000; i++) {
	    int num = i + (i % 10) + (i / 10 % 10) + (i / 100 % 10) + (i / 1000 % 10) + (i / 10000 % 10);
	    if (num > 10000) {
		continue;
	    } else {
		list[num - 1]++;
	    }
	}
	for (int i = 1; i <= 10000; i++) {
	    if (list[i - 1] == 0) {
		System.out.println(i);
	    }
	}
    }
}
