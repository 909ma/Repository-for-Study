
# C 언어 문법 정리

## 1. 기본 문법

### Hello World

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### 변수

```c
int a = 5;        // 정수형 변수
float b = 3.14;   // 실수형 변수
char c = 'A';     // 문자형 변수
```

### 입력과 출력

```c
#include <stdio.h>

int main() {
    int x;
    printf("Enter an integer: ");
    scanf("%d", &x);
    printf("You entered: %d\n", x);
    return 0;
}
```

### 조건문

```c
int x = 10;

if (x > 0) {
    printf("x is positive\n");
} else if (x == 0) {
    printf("x is zero\n");
} else {
    printf("x is negative\n");
}
```

### 반복문

#### for 문

```c
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}
```

#### while 문

```c
int i = 0;
while (i < 10) {
    printf("%d\n", i);
    i++;
}
```

#### do-while 문

```c
int i = 0;
do {
    printf("%d\n", i);
    i++;
} while (i < 10);
```

## 2. 함수

### 함수 선언과 정의

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 4);
    printf("Result: %d\n", result);
    return 0;
}
```

## 3. 배열과 문자열

### 배열

```c
int myArray[5] = {1, 2, 3, 4, 5};

for (int i = 0; i < 5; i++) {
    printf("%d\n", myArray[i]);
}
```

### 문자열

```c
#include <stdio.h>

int main() {
    char str[] = "Hello, World!";
    printf("%s\n", str);
    return 0;
}
```

## 4. 포인터와 참조

### 포인터

```c
int var = 20;
int *ptr = &var;

printf("var: %d\n", var);
printf("ptr: %p\n", ptr);
printf("*ptr: %d\n", *ptr);
```

## 5. 파일 입출력

### 파일 쓰기

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("example.txt", "w");
    if (fp != NULL) {
        fprintf(fp, "This is a line.\n");
        fprintf(fp, "This is another line.\n");
        fclose(fp);
    }
    return 0;
}
```

### 파일 읽기

```c
#include <stdio.h>

int main() {
    char line[100];
    FILE *fp = fopen("example.txt", "r");
    if (fp != NULL) {
        while (fgets(line, sizeof(line), fp)) {
            printf("%s", line);
        }
        fclose(fp);
    }
    return 0;
}
```

## 6. 구조체

### 구조체 선언 및 사용

```c
#include <stdio.h>
#include <string.h>

struct Person {
    char name[50];
    int age;
};

int main() {
    struct Person person1;
    strcpy(person1.name, "John Doe");
    person1.age = 30;

    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);

    return 0;
}
```

## 7. 예외 처리

C 언어는 직접적인 예외 처리 메커니즘을 제공하지 않지만, 오류 코드를 반환하고 검사하는 방식으로 처리할 수 있습니다.

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("non_existent_file.txt", "r");
    if (fp == NULL) {
        perror("Error opening file");
        return -1;
    }
    fclose(fp);
    return 0;
}
```
