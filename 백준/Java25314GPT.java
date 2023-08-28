/*
	@Author   : 909ma
	@Date     : 2023. 5. 18
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java25314GPT {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalNumbers = scanner.nextInt();
        scanner.close();
        
        if (totalNumbers % 4 != 0 || totalNumbers < 4 || totalNumbers > 1000) {
            System.out.println("ERROR: Invalid input for total numbers");
            return;
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < totalNumbers / 4; i++) {
            sb.append("long ");
        }
        sb.append("int");
        
        System.out.println(sb.toString());
    }
}
