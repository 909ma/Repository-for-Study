/*
 * @Author : 909ma
 * 
 * @Date : 2023. 5. 19
 * 
 * @Function :
 */
package practice;

import java.util.Scanner;

public class Java11720 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int count = scanner.nextInt();
    if (count < 1 || count > 100) {
      System.out.println("ERROR");
      scanner.close();
      return;
    }

    scanner.nextLine();
    String inputString = scanner.nextLine();
    if (inputString.length() != count) {
      System.out.println("ERROR");
      scanner.close();
      return;
    }
    scanner.close();

    int sum = 0;
    for (int i = 0; i < count; i++) {
      // sum += Integer.parseInt(inputString.charAt(i));//이거 안 됨
      // sum += Integer.parseInt(String.valueOf(inputString.charAt(i)));
      sum += Character.getNumericValue(inputString.charAt(i));
    }

    System.out.println(sum);
  }
}
