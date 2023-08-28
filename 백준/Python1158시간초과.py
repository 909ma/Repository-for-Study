N, K = map(int, input().split())
queue = []
answer = []
for i in range(N):
    queue.append(i + 1)

while len(queue) > 0:
    for _ in range(K - 1):
        temp = queue.pop(0)
        queue.append(temp)
    temp = queue.pop(0)
    answer.append(temp)

print("<", end="")
print(*answer, sep=", ", end="")
print(">")
