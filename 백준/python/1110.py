num = int(input())
checkNum = num
count = 0
while True:
    count += 1
    if num < 10:
        a = 0
        b = num
    else:
        a = num // 10
        b = num % 10
    sum1 = a + b
    sum1 %= 10
    sum1 = 10 * b + sum1

    if sum1 == checkNum:
        break
    else:
        num = sum1

print(count)
