/*
    @Author   : 909ma
    @Date     : 2023. 5. 19
    @Function : 
 */
package practice;

import java.util.Scanner;

public class Java27866 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine();
        if (inputString.length() > 1000) {
            System.out.println("ERROR: Input length exceeds the limit");
            scanner.close();
            return;
        }
        int index = scanner.nextInt();

        if (index < 1 || index > inputString.length()) {
            System.out.println("ERROR: Index out of range");
            scanner.close();
            return;
        }

        System.out.println(inputString.charAt(index-1));
        scanner.close();
    }
}
