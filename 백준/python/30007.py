test_cases = int(input())
for _ in range(test_cases):
    a, b, x = map(int, input().split())
    print(a*(x-1)+b)
