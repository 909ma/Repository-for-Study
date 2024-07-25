/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.ArrayList;
import java.util.Scanner;

public class Java10952 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		ArrayList<Integer> A = new ArrayList<Integer>();
		ArrayList<Integer> B = new ArrayList<Integer>();
		ArrayList<Integer> sum = new ArrayList<Integer>();
		int temp;
		int index = 0;
		for(int i = 0;;i++) {
			temp = Scanner.nextInt();
			if(temp<0) {
				System.out.println("ERROR A");
				Scanner.close();
				return;
			}
			A.add(temp);
			
			temp = Scanner.nextInt();
			if(temp>=10) {
				System.out.println("ERROR B");
				Scanner.close();
				return;
			}
			B.add(temp);
			temp = A.get(i) + B.get(i);
			
			sum.add(temp);
			index ++;
			
			if(A.get(i)==B.get(i)&&A.get(i)==0) {
				break;
			}
		}
		Scanner.close();
		
		for(int i = 0; i <index-1;i++) {
			System.out.println(sum.get(i));
		}
	}

}
