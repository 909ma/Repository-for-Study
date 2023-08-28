def num(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1


testCase = int(input())
for i in range(testCase):
    M, N, x, y = map(int, input().split())
    print(num(M, N, x, y))
