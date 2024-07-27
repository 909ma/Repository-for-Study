
# TypeScript 문법 정리

## 1. 기본 문법

### Hello World

```typescript
console.log("Hello, World!");
```

### 변수

```typescript
let a: number = 5;            // 정수형 변수
let b: number = 3.14;         // 실수형 변수
let c: string = 'A';          // 문자형 변수
let s: string = "Hello";      // 문자열 변수
let flag: boolean = true;     // 불리언 변수
```

### 입력과 출력

TypeScript는 브라우저 또는 Node.js 환경에서 주로 사용되므로, 입력을 받는 방법은 환경에 따라 다릅니다. 여기서는 Node.js 환경을 가정합니다.

```typescript
import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter an integer: ', (answer) => {
    let x: number = parseInt(answer);
    console.log(`You entered: ${x}`);
    rl.close();
});
```

### 조건문

```typescript
let x: number = 10;

if (x > 0) {
    console.log("x is positive");
} else if (x === 0) {
    console.log("x is zero");
} else {
    console.log("x is negative");
}
```

### 반복문

#### for 문

```typescript
for (let i: number = 0; i < 10; i++) {
    console.log(i);
}
```

#### while 문

```typescript
let i: number = 0;
while (i < 10) {
    console.log(i);
    i++;
}
```

#### do-while 문

```typescript
let i: number = 0;
do {
    console.log(i);
    i++;
} while (i < 10);
```

## 2. 함수

### 함수 선언과 정의

```typescript
function add(a: number, b: number): number {
    return a + b;
}

let result: number = add(3, 4);
console.log(`Result: ${result}`);
```

## 3. 클래스와 객체

### 클래스 정의

```typescript
class MyClass {
    myNumber: number;

    constructor(myNumber: number) {
        this.myNumber = myNumber;
    }

    myFunction(): void {
        console.log("Hello World!");
    }
}
```

### 객체 생성 및 사용

```typescript
let myObj = new MyClass(15);
myObj.myFunction();
console.log(myObj.myNumber);
```

## 4. 배열과 튜플

### 배열

```typescript
let myArray: number[] = [1, 2, 3, 4, 5];

for (let i: number = 0; i < myArray.length; i++) {
    console.log(myArray[i]);
}
```

### 튜플

```typescript
let myTuple: [string, number] = ["Hello", 42];
console.log(myTuple[0]);
console.log(myTuple[1]);
```

## 5. 인터페이스

### 인터페이스 정의 및 사용

```typescript
interface Person {
    name: string;
    age: number;
    married: boolean;
}

let john: Person = {
    name: "John",
    age: 30,
    married: true
};

console.log(john);
```

## 6. 기본적인 비동기 처리

### Promise 사용

```typescript
function delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

delay(1000).then(() => console.log("1 second passed"));
```

### async/await 사용

```typescript
async function asyncDelay(ms: number): Promise<void> {
    await delay(ms);
    console.log("1 second passed with async/await");
}

asyncDelay(1000);
```

## 7. 파일 입출력 (Node.js 환경)

### 파일 쓰기

```typescript
import * as fs from 'fs';

let data = "This is a line.\nThis is another line.\n";
fs.writeFileSync('example.txt', data);
```

### 파일 읽기

```typescript
import * as fs from 'fs';

let data = fs.readFileSync('example.txt', 'utf8');
console.log(data);
```
