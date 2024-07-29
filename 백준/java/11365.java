import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            String message = scanner.nextLine();

            if (message.equals("END")) {
                break;
            }

            for (int i = message.length() - 1; i >= 0; i--) {
                System.out.print(message.charAt(i));
            }
            System.out.println();
        }

        scanner.close();
    }
}
