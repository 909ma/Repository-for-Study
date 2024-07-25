import sys

input = sys.stdin.readline
# .rstrip()

line = list(map(int, input().split()))
M = line[0]
N = line[1]
dic = {}
for i in range(M):
    line = list(map(str, input().split()))
    dic[line[0]] = line[1]

for _ in range(N):
    line = input().rstrip()
    pw = dic[line]
    print(pw)
