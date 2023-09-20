X, Y = map(int, input().split())
Z_origin = int(Y / X * 100)
answer = X**2 / (99*X - 100*Y)

if X + answer:
    answer = answer // 1 + int(bool(answer % 1))
    print(int(answer))
else:
    print(-1)
