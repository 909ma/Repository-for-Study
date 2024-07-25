num = [0] * 10
line = input()
length = len(line)
for i in range(0, length, 1):
    num[int(line[i])] += 1

num6 = num[6]
num[6] = -1
num9 = num[9]
num[9] = -1

maxNum = max(num)
if maxNum * 2 >= num6 + num9:
    pass
else:
    if (num6 + num9) % 2 == 0:
        maxNum = (num6 + num9) // 2
    else:
        maxNum = (num6 + num9) // 2 + 1

print(maxNum)
