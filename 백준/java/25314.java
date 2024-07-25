/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java25314 {
    public static void main(String[] args) {
    	Scanner Scanner = new Scanner(System.in);
    	int N = Scanner.nextInt();
    	if(N%4!=0 || N<4||N>1000) {
    		System.out.println("ERROR N");
    		Scanner.close();
    		return;
    	}
    	Scanner.close();
    	for(int i = 0; i < N/4; i++) {
    		System.out.print("long ");
    	}
    	System.out.println("int");
    }
}
