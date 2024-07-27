
# C++ 문법 정리

## 1. 기본 문법

### Hello World

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### 변수

```cpp
int a = 5;        // 정수형 변수
double b = 3.14;  // 실수형 변수
char c = 'A';     // 문자형 변수
std::string s = "Hello";  // 문자열 변수 (C++11 이상)
```

### 입력과 출력

```cpp
#include <iostream>

int main() {
    int x;
    std::cout << "Enter an integer: ";
    std::cin >> x;
    std::cout << "You entered: " << x << std::endl;
    return 0;
}
```

### 조건문

```cpp
int x = 10;

if (x > 0) {
    std::cout << "x is positive" << std::endl;
} else if (x == 0) {
    std::cout << "x is zero" << std::endl;
} else {
    std::cout << "x is negative" << std::endl;
}
```

### 반복문

#### for 문

```cpp
for (int i = 0; i < 10; i++) {
    std::cout << i << std::endl;
}
```

#### while 문

```cpp
int i = 0;
while (i < 10) {
    std::cout << i << std::endl;
    i++;
}
```

#### do-while 문

```cpp
int i = 0;
do {
    std::cout << i << std::endl;
    i++;
} while (i < 10);
```

## 2. 함수

### 함수 선언과 정의

```cpp
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 4);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
```

## 3. 클래스와 객체

### 클래스 정의

```cpp
class MyClass {
public:
    int myNumber;
    void myFunction() {
        std::cout << "Hello World!" << std::endl;
    }
};
```

### 객체 생성 및 사용

```cpp
#include <iostream>

class MyClass {
public:
    int myNumber;
    void myFunction() {
        std::cout << "Hello World!" << std::endl;
    }
};

int main() {
    MyClass myObj;
    myObj.myNumber = 15;
    myObj.myFunction();
    std::cout << myObj.myNumber << std::endl;
    return 0;
}
```

## 4. 포인터와 참조

### 포인터

```cpp
int var = 20;
int *ptr = &var;

std::cout << "var: " << var << std::endl;
std::cout << "ptr: " << ptr << std::endl;
std::cout << "*ptr: " << *ptr << std::endl;
```

### 참조

```cpp
int var = 20;
int &ref = var;

std::cout << "var: " << var << std::endl;
std::cout << "ref: " << ref << std::endl;
```

## 5. 배열과 문자열

### 배열

```cpp
int myArray[5] = {1, 2, 3, 4, 5};

for (int i = 0; i < 5; i++) {
    std::cout << myArray[i] << std::endl;
}
```

### 문자열

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, World!";
    std::cout << str << std::endl;
    return 0;
}
```

## 6. 파일 입출력

### 파일 쓰기

```cpp
#include <fstream>

int main() {
    std::ofstream myfile("example.txt");
    if (myfile.is_open()) {
        myfile << "This is a line.
";
        myfile << "This is another line.
";
        myfile.close();
    }
    return 0;
}
```

### 파일 읽기

```cpp
#include <fstream>
#include <string>
#include <iostream>

int main() {
    std::string line;
    std::ifstream myfile("example.txt");
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            std::cout << line << std::endl;
        }
        myfile.close();
    }
    return 0;
}
```

## 7. 예외 처리

```cpp
#include <iostream>

int main() {
    try {
        int* myArray = new int[1000];
        // 배열 사용
        delete[] myArray;
    } catch (std::bad_alloc& e) {
        std::cout << "Allocation failed: " << e.what() << std::endl;
    }
    return 0;
}
```
