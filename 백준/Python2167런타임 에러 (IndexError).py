a, b = map(int, input().split())
line = [a, b]  # 고친 부분
for i in range(0, a, 1):
    line[i] = list(map(int, input().split()))

testCase = int(input())
for _ in range(testCase):
    x1, y1, x2, y2 = map(int, input().split())
    sum1 = 0
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            sum1 += line[i][j]
    print(sum1)
