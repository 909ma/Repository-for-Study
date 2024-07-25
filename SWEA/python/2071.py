test_cases = int(input())
for i in range(test_cases):
    num = list(map(int, input().split()))
    print(f"#{i + 1} {round(sum([item for item in num]) / 10)}")
