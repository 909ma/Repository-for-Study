/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java25304 {

	public static void main(String[] args) {
		Scanner Scanner = new Scanner(System.in);
		int sum = Scanner.nextInt();//총 금액
		if(sum<1||sum>1000000000) {
			System.out.println("ERROR sum");
			Scanner.close();
			return;
		}
		int count = Scanner.nextInt();//개수
		if(count<1||count>100) {
			System.out.println("ERROR count");
			Scanner.close();
			return;
		}
		int[] price = new int[count];//개별 상품 가격
		int[] productCount = new int[count];//개별 상품 개수
		int sumIf = 0;//총합 확인 변수
		for(int i = 0; i < count; i++) {
			price[i] = Scanner.nextInt();
			if(price[i] <1 || price[i] > 1000000) {
			System.out.println("ERROR price");
			Scanner.close();
			return;
		}
			productCount[i] = Scanner.nextInt();
			if(productCount[i]<1||productCount[i]>10) {
				System.out.println("ERROR productCount");
				Scanner.close();
				return;
			}
			sumIf += price[i]*productCount[i];
		}
		Scanner.close();
		if(sum==sumIf) {
			System.out.println("Yes");
		}
		else {
			System.out.println("No");
		}
	}

}
