NumList = [[] for _ in range(200001)]
size = int(input())

for i in range(size):
    a, b = map(int, input().split())
    NumList[a + 100000].append(b)

for i in range(200001):
    NumList[i].sort(reverse=False)
    size2 = len(NumList[i])
    if size2 == 0:
        continue
    else:
        for j in range(size2):
            print(f"{i-100000} {NumList[i][j]}")

"""
size = int(input())
points = []

for _ in range(size):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()

for x, y in points:
    print(x, y)

굳이 개고생할 필요없이 다차원에서도 sort가 되네...
"""

"""
a=int(input())
b=[list(map(int,input().split())) for i in range(a)]
b.sort()
for i in b:
    print(*i)
    
이게 진짜 대박이네    
"""
