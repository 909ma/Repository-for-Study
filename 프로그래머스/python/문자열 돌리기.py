from collections import deque

str = input()
output = deque(str)
size = len(str)

for _ in range(size):
    print(output.popleft())


"""
print('\n'.join(input()))
이런 풀이도 다 있네
"""
