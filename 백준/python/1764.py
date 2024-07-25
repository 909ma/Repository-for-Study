import sys

input = sys.stdin.readline
# .rstrip()

N, M = map(int, input().rstrip().split())
answer = []

list1 = set()
for i in range(N):
    list1.add(input().rstrip())

for i in range(N):
    name = input().rstrip()
    if name in list1:
        answer.append(name)

answer = sorted(answer)
size = len(answer)
print(size)
print(*answer, sep='\n')

