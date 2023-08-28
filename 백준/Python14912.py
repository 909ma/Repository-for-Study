n, d = map(int, input().split())
arr = []
for i in range(1, n + 1, 1):
    arr.append(i)

numList = [0] * 10
for i in range(0, n, 1):
    length = len(str(arr[i]))
    for j in range(0, length, 1):
        temp = arr[i] % 10
        numList[temp] += 1
        arr[i] = arr[i] // 10

print(numList[d])
