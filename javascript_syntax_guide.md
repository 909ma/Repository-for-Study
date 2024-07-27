
# JavaScript 문법 정리

## 1. 기본 문법

### Hello World

```javascript
console.log("Hello, World!");
```

### 변수

```javascript
var a = 5;             // 옛날 방식의 변수 선언
let b = 3.14;          // ES6 이후 도입된 블록 스코프 변수
const c = 'A';         // 상수, 값 변경 불가
let s = "Hello";       // 문자열 변수
let flag = true;       // 불리언 변수
```

### 입력과 출력

JavaScript는 주로 웹 브라우저에서 사용되기 때문에, 입력을 받는 방법은 `prompt`를 사용합니다. Node.js 환경에서는 `readline` 모듈을 사용할 수 있습니다.

#### 브라우저 환경

```javascript
let x = prompt("Enter an integer: ");
console.log(`You entered: ${x}`);
```

#### Node.js 환경

```javascript
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter an integer: ', (answer) => {
    let x = parseInt(answer);
    console.log(`You entered: ${x}`);
    rl.close();
});
```

### 조건문

```javascript
let x = 10;

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

```javascript
for (let i = 0; i < 10; i++) {
    console.log(i);
}
```

#### while 문

```javascript
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}
```

#### do-while 문

```javascript
let i = 0;
do {
    console.log(i);
    i++;
} while (i < 10);
```

## 2. 함수

### 함수 선언과 정의

```javascript
function add(a, b) {
    return a + b;
}

let result = add(3, 4);
console.log(`Result: ${result}`);
```

### 화살표 함수 (ES6)

```javascript
const add = (a, b) => a + b;

let result = add(3, 4);
console.log(`Result: ${result}`);
```

## 3. 객체와 클래스

### 객체 리터럴

```javascript
let person = {
    name: "John",
    age: 30,
    married: true
};

console.log(person);
```

### 클래스 정의 및 사용 (ES6)

```javascript
class MyClass {
    constructor(myNumber) {
        this.myNumber = myNumber;
    }

    myFunction() {
        console.log("Hello World!");
    }
}

let myObj = new MyClass(15);
myObj.myFunction();
console.log(myObj.myNumber);
```

## 4. 배열과 객체

### 배열

```javascript
let myArray = [1, 2, 3, 4, 5];

for (let i = 0; i < myArray.length; i++) {
    console.log(myArray[i]);
}
```

### 객체

```javascript
let person = {
    name: "John",
    age: 30,
    married: true
};

console.log(person.name);
console.log(person.age);
console.log(person.married);
```

## 5. 비동기 처리

### Promise 사용

```javascript
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

delay(1000).then(() => console.log("1 second passed"));
```

### async/await 사용

```javascript
async function asyncDelay(ms) {
    await delay(ms);
    console.log("1 second passed with async/await");
}

asyncDelay(1000);
```

## 6. 파일 입출력 (Node.js 환경)

### 파일 쓰기

```javascript
const fs = require('fs');

let data = "This is a line.\nThis is another line.\n";
fs.writeFileSync('example.txt', data);
```

### 파일 읽기

```javascript
const fs = require('fs');

let data = fs.readFileSync('example.txt', 'utf8');
console.log(data);
```
