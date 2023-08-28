import math
import sys

n = int(sys.stdin.readline().rstrip())
answer = [0] * (n + 1)
for i in range(n+1):
    if i == 1:
        answer[i] = 1
    elif i == 2:
        answer[i] = 3
    else:
        answer[i] = answer[i - 2] * 2 + answer[i-1]

print(answer[n] % 10007)
