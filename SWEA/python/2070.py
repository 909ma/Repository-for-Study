test_cases = int(input())
for i in range(test_cases):
    a, b = map(int, input().split())
    if a > b:
        output = '>'
    elif a == b:
        output = '='
    else:
        output = '<'
    print(f"#{i + 1} {output}")
