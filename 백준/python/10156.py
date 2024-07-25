a, b, c = map(int, input().split())
print(a * b - c) if c - a * b <= 0 else print(0)
