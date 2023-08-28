/*
 	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java25304GPT {
	 public static void main(String[] args) {
	        Scanner scanner = new Scanner(System.in);
	        int totalAmount = scanner.nextInt();
	        if (totalAmount < 1 || totalAmount > 1000000000) {
	            System.out.println("ERROR sum");
	            scanner.close();
	            return;
	        }

	        int productCount = scanner.nextInt();
	        if (productCount < 1 || productCount > 100) {
	            System.out.println("ERROR count");
	            scanner.close();
	            return;
	        }

	        int sumIf = 0;
	        for (int i = 0; i < productCount; i++) {
	            int productPrice = scanner.nextInt();
	            if (productPrice < 1 || productPrice > 1000000) {
	                System.out.println("ERROR price");
	                scanner.close();
	                return;
	            }

	            int productQuantity = scanner.nextInt();
	            if (productQuantity < 1 || productQuantity > 10) {
	                System.out.println("ERROR productCount");
	                scanner.close();
	                return;
	            }

	            sumIf += productPrice * productQuantity;
	        }

	        scanner.close();

	        if (totalAmount == sumIf) {
	            System.out.println("Yes");
	        } else {
	            System.out.println("No");
	        }
	    }
}
