
# C# 문법 정리

## 1. 기본 문법

### Hello World

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
    }
}
```

### 변수

```csharp
int a = 5;            // 정수형 변수
double b = 3.14;      // 실수형 변수
char c = 'A';         // 문자형 변수
string s = "Hello";   // 문자열 변수
bool flag = true;     // 불리언 변수
```

### 입력과 출력

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter an integer: ");
        int x = int.Parse(Console.ReadLine());
        Console.WriteLine("You entered: " + x);
    }
}
```

### 조건문

```csharp
int x = 10;

if (x > 0)
{
    Console.WriteLine("x is positive");
}
else if (x == 0)
{
    Console.WriteLine("x is zero");
}
else
{
    Console.WriteLine("x is negative");
}
```

### 반복문

#### for 문

```csharp
for (int i = 0; i < 10; i++)
{
    Console.WriteLine(i);
}
```

#### while 문

```csharp
int i = 0;
while (i < 10)
{
    Console.WriteLine(i);
    i++;
}
```

#### do-while 문

```csharp
int i = 0;
do
{
    Console.WriteLine(i);
    i++;
} while (i < 10);
```

## 2. 함수

### 함수 선언과 정의

```csharp
using System;

class Program
{
    static int Add(int a, int b)
    {
        return a + b;
    }

    static void Main()
    {
        int result = Add(3, 4);
        Console.WriteLine("Result: " + result);
    }
}
```

## 3. 클래스와 객체

### 클래스 정의

```csharp
class MyClass
{
    public int MyNumber;
    public void MyFunction()
    {
        Console.WriteLine("Hello World!");
    }
}
```

### 객체 생성 및 사용

```csharp
using System;

class MyClass
{
    public int MyNumber;
    public void MyFunction()
    {
        Console.WriteLine("Hello World!");
    }
}

class Program
{
    static void Main()
    {
        MyClass myObj = new MyClass();
        myObj.MyNumber = 15;
        myObj.MyFunction();
        Console.WriteLine(myObj.MyNumber);
    }
}
```

## 4. 배열과 문자열

### 배열

```csharp
int[] myArray = {1, 2, 3, 4, 5};

for (int i = 0; i < myArray.Length; i++)
{
    Console.WriteLine(myArray[i]);
}
```

### 문자열

```csharp
using System;

class Program
{
    static void Main()
    {
        string str = "Hello, World!";
        Console.WriteLine(str);
    }
}
```

## 5. 파일 입출력

### 파일 쓰기

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (StreamWriter writer = new StreamWriter("example.txt"))
        {
            writer.WriteLine("This is a line.");
            writer.WriteLine("This is another line.");
        }
    }
}
```

### 파일 읽기

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (StreamReader reader = new StreamReader("example.txt"))
        {
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                Console.WriteLine(line);
            }
        }
    }
}
```

## 6. 예외 처리

```csharp
using System;

class Program
{
    static void Main()
    {
        try
        {
            int[] myArray = new int[1000];
            // 배열 사용
        }
        catch (Exception e)
        {
            Console.WriteLine("An error occurred: " + e.Message);
        }
    }
}
```
