from collections import deque

N = int(input())

queue = deque(range(1, N + 1))

while len(queue) > 0:
    print(queue.popleft(), end=' ')
    if len(queue) > 0:
        queue.append(queue.popleft())

print()
