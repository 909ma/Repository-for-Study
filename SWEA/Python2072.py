test_cases = int(input())
for i in range(test_cases):
    num = list(map(int, input().split()))
    print(f"#{i + 1} {sum([item for item in num if item % 2 == 1])}")
