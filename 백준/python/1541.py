import sys

num = sys.stdin.readline().rstrip().split("-")
result = sum(map(int, num[0].split('+')))
for i in num[1:]:
    result -= sum(map(int, i.split('+')))
print(result)
