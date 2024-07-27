
# Java 문법 정리

## 1. 기본 문법

### Hello World

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### 변수

```java
int a = 5;            // 정수형 변수
double b = 3.14;      // 실수형 변수
char c = 'A';         // 문자형 변수
String s = "Hello";   // 문자열 변수
boolean flag = true;  // 불리언 변수
```

### 입력과 출력

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int x = scanner.nextInt();
        System.out.println("You entered: " + x);
    }
}
```

### 조건문

```java
int x = 10;

if (x > 0) {
    System.out.println("x is positive");
} else if (x == 0) {
    System.out.println("x is zero");
} else {
    System.out.println("x is negative");
}
```

### 반복문

#### for 문

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

#### while 문

```java
int i = 0;
while (i < 10) {
    System.out.println(i);
    i++;
}
```

#### do-while 문

```java
int i = 0;
do {
    System.out.println(i);
    i++;
} while (i < 10);
```

## 2. 함수

### 함수 선언과 정의

```java
public class Main {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int result = add(3, 4);
        System.out.println("Result: " + result);
    }
}
```

## 3. 클래스와 객체

### 클래스 정의

```java
public class MyClass {
    public int myNumber;
    
    public void myFunction() {
        System.out.println("Hello World!");
    }
}
```

### 객체 생성 및 사용

```java
public class MyClass {
    public int myNumber;
    
    public void myFunction() {
        System.out.println("Hello World!");
    }
}

public class Main {
    public static void main(String[] args) {
        MyClass myObj = new MyClass();
        myObj.myNumber = 15;
        myObj.myFunction();
        System.out.println(myObj.myNumber);
    }
}
```

## 4. 배열과 문자열

### 배열

```java
int[] myArray = {1, 2, 3, 4, 5};

for (int i = 0; i < myArray.length; i++) {
    System.out.println(myArray[i]);
}
```

### 문자열

```java
public class Main {
    public static void main(String[] args) {
        String str = "Hello, World!";
        System.out.println(str);
    }
}
```

## 5. 파일 입출력

### 파일 쓰기

```java
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try {
            FileWriter writer = new FileWriter("example.txt");
            writer.write("This is a line.\n");
            writer.write("This is another line.\n");
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 파일 읽기

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("example.txt"));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## 6. 예외 처리

```java
public class Main {
    public static void main(String[] args) {
        try {
            int[] myArray = new int[1000];
            // 배열 사용
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}
```
