/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.math.BigDecimal;
import java.util.Scanner;

public class Java10757 {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	BigDecimal A = new BigDecimal(scanner.next());
	BigDecimal B = new BigDecimal(scanner.next());
	scanner.close();

	BigDecimal sum = A.add(B);
	System.out.println(sum);
    }
}
