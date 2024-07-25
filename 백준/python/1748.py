n = int(input())
count = 0
i = 1
while i <= n:
    count += (n - i + 1)
    i *= 10
print(count)
