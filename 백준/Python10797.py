date = int(input())
carList = list(map(int, input().split(" ")))
count = 0
size = len(carList)
for i in range(0, size, 1):
    if carList[i] == date:
        count += 1
print(count)
