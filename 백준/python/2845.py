num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 = num1[0] * num1[1]

for i in range(0, 5, 1):
    num2[i] = num2[i] - num3

print(*num2)
