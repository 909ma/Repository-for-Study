
# Swift 문법 정리

## 1. 기본 문법

### Hello World

```swift
print("Hello, World!")
```

### 변수

```swift
var a: Int = 5          // 정수형 변수
var b: Double = 3.14    // 실수형 변수
var c: Character = "A"  // 문자형 변수
var s: String = "Hello" // 문자열 변수
var flag: Bool = true   // 불리언 변수
```

### 입력과 출력

Swift에서는 입력을 받는 방법이 직접적으로 제공되지 않지만, `readLine()`을 사용할 수 있습니다.

```swift
print("Enter an integer: ", terminator: "")
if let input = readLine(), let x = Int(input) {
    print("You entered: \(x)")
}
```

### 조건문

```swift
let x = 10

if x > 0 {
    print("x is positive")
} else if x == 0 {
    print("x is zero")
} else {
    print("x is negative")
}
```

### 반복문

#### for 문

```swift
for i in 0..<10 {
    print(i)
}
```

#### while 문

```swift
var i = 0
while i < 10 {
    print(i)
    i += 1
}
```

#### repeat-while 문

```swift
var i = 0
repeat {
    print(i)
    i += 1
} while i < 10
```

## 2. 함수

### 함수 선언과 정의

```swift
func add(a: Int, b: Int) -> Int {
    return a + b
}

let result = add(a: 3, b: 4)
print("Result: \(result)")
```

## 3. 클래스와 구조체

### 클래스 정의 및 사용

```swift
class MyClass {
    var myNumber: Int
    
    init(myNumber: Int) {
        self.myNumber = myNumber
    }
    
    func myFunction() {
        print("Hello World!")
    }
}

let myObj = MyClass(myNumber: 15)
myObj.myFunction()
print(myObj.myNumber)
```

### 구조체 정의 및 사용

```swift
struct MyStruct {
    var myNumber: Int
    
    func myFunction() {
        print("Hello World!")
    }
}

let myObj = MyStruct(myNumber: 15)
myObj.myFunction()
print(myObj.myNumber)
```

## 4. 배열과 딕셔너리

### 배열

```swift
let myArray = [1, 2, 3, 4, 5]

for i in myArray {
    print(i)
}
```

### 딕셔너리

```swift
let myDict = ["name": "John", "age": 30, "married": true] as [String : Any]

for (key, value) in myDict {
    print("\(key): \(value)")
}
```

## 5. 옵셔널

### 옵셔널 변수

```swift
var optionalVar: Int? = nil
optionalVar = 10

if let unwrappedVar = optionalVar {
    print("Value is \(unwrappedVar)")
} else {
    print("Value is nil")
}
```

## 6. 에러 처리

### 에러 정의 및 던지기

```swift
enum MyError: Error {
    case runtimeError(String)
}

func throwError() throws {
    throw MyError.runtimeError("This is a runtime error")
}

do {
    try throwError()
} catch MyError.runtimeError(let errorMessage) {
    print("Error: \(errorMessage)")
}
```

## 7. 클로저

### 기본 클로저 사용

```swift
let add = { (a: Int, b: Int) -> Int in
    return a + b
}

let result = add(3, 4)
print("Result: \(result)")
```

### 간단한 클로저 사용

```swift
let numbers = [1, 2, 3, 4, 5]
let doubled = numbers.map { $0 * 2 }
print(doubled)
```
