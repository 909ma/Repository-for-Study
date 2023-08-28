/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java10101 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int angle1 = scanner.nextInt();
	int angle2 = scanner.nextInt();
	int angle3 = scanner.nextInt();
	scanner.close();
	if (angle1 == angle2 && angle1 == angle3 && angle1 == 60) {
	    System.out.println("Equilateral");
	} else if ((angle1 + angle2 + angle3) == 180 && (angle1 == angle2 || angle1 == angle3 || angle2 == angle3)) {
	    System.out.println("Isosceles");
	} else if ((angle1 + angle2 + angle3) == 180 && (angle1 != angle2 && angle1 != angle3 && angle2 != angle3)) {
	    System.out.println("Scalene");
	} else {
	    System.out.println("Error");
	}
    }
}
