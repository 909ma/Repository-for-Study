
# R 문법 정리

## 1. 기본 문법

### Hello World

```r
print("Hello, World!")
```

### 변수

```r
a <- 5          # 정수형 변수
b <- 3.14       # 실수형 변수
c <- 'A'        # 문자형 변수
s <- "Hello"    # 문자열 변수
flag <- TRUE    # 불리언 변수
```

### 입력과 출력

```r
x <- as.integer(readline(prompt="Enter an integer: "))
cat("You entered:", x, "
")
```

### 조건문

```r
x <- 10

if (x > 0) {
    print("x is positive")
} else if (x == 0) {
    print("x is zero")
} else {
    print("x is negative")
}
```

### 반복문

#### for 문

```r
for (i in 1:10) {
    print(i)
}
```

#### while 문

```r
i <- 1
while (i <= 10) {
    print(i)
    i <- i + 1
}
```

#### repeat 문

```r
i <- 1
repeat {
    print(i)
    i <- i + 1
    if (i > 10) {
        break
    }
}
```

## 2. 함수

### 함수 선언과 정의

```r
add <- function(a, b) {
    return (a + b)
}

result <- add(3, 4)
print(paste("Result:", result))
```

## 3. 벡터와 리스트

### 벡터

```r
myVector <- c(1, 2, 3, 4, 5)
print(myVector)
```

### 리스트

```r
myList <- list(name = "John", age = 30, married = TRUE)
print(myList)
```

## 4. 행렬과 데이터 프레임

### 행렬

```r
myMatrix <- matrix(1:9, nrow = 3, ncol = 3)
print(myMatrix)
```

### 데이터 프레임

```r
myDataFrame <- data.frame(
    name = c("John", "Jane", "Doe"),
    age = c(30, 25, 22),
    married = c(TRUE, FALSE, TRUE)
)
print(myDataFrame)
```

## 5. 파일 입출력

### 파일 쓰기

```r
myDataFrame <- data.frame(
    name = c("John", "Jane", "Doe"),
    age = c(30, 25, 22),
    married = c(TRUE, FALSE, TRUE)
)

write.csv(myDataFrame, file = "example.csv", row.names = FALSE)
```

### 파일 읽기

```r
myDataFrame <- read.csv("example.csv")
print(myDataFrame)
```

## 6. 기본 그래프 그리기

### 산점도

```r
x <- c(1, 2, 3, 4, 5)
y <- c(2, 3, 5, 7, 11)
plot(x, y, main = "Scatter Plot", xlab = "X-Axis", ylab = "Y-Axis")
```

### 히스토그램

```r
data <- c(1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5)
hist(data, main = "Histogram", xlab = "Values", ylab = "Frequency")
```

## 7. 기본 통계 함수

### 평균, 중간값, 표준편차

```r
data <- c(1, 2, 3, 4, 5)
mean(data)      # 평균
median(data)    # 중간값
sd(data)        # 표준편차
```
