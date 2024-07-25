max1 = 0
count = 0
for _ in range(4):
    out1, in1 = map(int, input().split(" "))
    count += in1
    count -= out1
    if max1 < count:
        max1 = count
print(max1)
