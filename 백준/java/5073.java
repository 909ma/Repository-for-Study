/*
	@Author   : 909ma
	@Date     : 2023. 5. 23
	@Function : 
 */
package practice;

import java.util.Scanner;

public class Java5073 {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	while (true) {
	    int angle1 = scanner.nextInt();
	    int angle2 = scanner.nextInt();
	    int angle3 = scanner.nextInt();
	    int max = angle1;
	    int noMax = 0;
	    if (angle1 >= angle2 && angle1 > angle3) {
		max = angle1;
		noMax = angle2 + angle3;
	    } else if (angle2 >= angle1 && angle2 > angle3) {
		max = angle2;
		noMax = angle1 + angle3;
	    } else {
		max = angle3;
		noMax = angle1 + angle2;
	    }

	    if (angle1 == angle2 && angle1 == angle3 && angle1 == 0) {
		break;
	    }

	    if (max >= noMax) {
		System.out.println("Invalid");
	    } else if (angle1 == angle2 && angle1 == angle3) {
		System.out.println("Equilateral");
	    } else if (angle1 == angle2 || angle1 == angle3 || angle2 == angle3) {
		System.out.println("Isosceles");
	    } else if (angle1 != angle2 && angle1 != angle3 && angle2 != angle3) {
		System.out.println("Scalene");
	    } else {
		System.out.println("Error");
	    }
	}
	scanner.close();
    }
}
