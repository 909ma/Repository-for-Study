A = int(input())
B = int(input())
C = int(input())
num = str(A * B * C)
numList = [0] * 10
for i in range(0, 10, 1):
    numList[i] = num.count(str(i))
print(*numList, sep="\n")
