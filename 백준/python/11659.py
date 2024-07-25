import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

sumNum = [0] * (N + 1)
for i in range(1, N + 1):
    sumNum[i] = sumNum[i - 1] + num[i - 1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer = sumNum[b] - sumNum[a - 1]
    print(answer)
