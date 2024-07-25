/*
	@Author   : 909ma
	@Date     : 2023. 5. 22
	@Function : 런타임 에러 (NoSuchElement)
	
`java.util.NoSuchElementException` 예외가 발생하는 이유는 입력을 기다리는 `scanner.nextLine()` 메소드를 호출할 때 입력이 없을 경우입니다. 

해당 코드에서는 `MAX_NUMBER`만큼 반복하면서 `scanner.nextLine()`을 호출하고 있습니다. 그러나 입력이 `MAX_NUMBER`보다 적을 경우, 예를 들어 입력이 3줄만 주어졌을 때, 4번째 반복에서 `scanner.nextLine()`을 호출하면서 `NoSuchElementException`가 발생합니다.

입력의 개수에 상관없이 입력을 계속 받고, 빈 줄이 나타나면 입력을 종료하는 방식으로 수정할 수 있습니다. 예를 들어, `scanner.hasNextLine()` 메소드를 사용하여 입력이 있는지 확인하고, 반복문을 종료하는 방식으로 코드를 변경할 수 있습니다.

```java
import java.util.Scanner;

public class Java11718 {
    public static void main(String[] args) {
        final int MAX_NUMBER = 100;
        String[] inputString = new String[MAX_NUMBER];

        Scanner scanner = new Scanner(System.in);
        int index = 0;
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.isEmpty()) {
                break;
            }
            inputString[index] = line;
            index++;
        }
        scanner.close();

        for (String str : inputString) {
            if (str == null) {
                break;
            }
            System.out.println(str);
        }
    }
}
```

이렇게 수정하면 `NoSuchElementException` 예외가 발생하지 않고, 입력이 주어진 대로 출력될 것입니다.

 */
package practice;

import java.util.Scanner;

public class Java11718 {
    public static void main(String[] args) {
	final int MAX_NUMBER = 100;
	String[] inputString = new String[MAX_NUMBER];

	Scanner scanner = new Scanner(System.in);
	for (int i = 0; i < MAX_NUMBER; i++) {
	    String line = scanner.nextLine();
	    if (line.isEmpty()) {
		break;
	    }
	    inputString[i] = line;
	}
	scanner.close();

	for (String str : inputString) {
	    if (str == null) {
		break;
	    }
	    System.out.println(str);
	}
    }
}
