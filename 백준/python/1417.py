testCase = int(input())
count = 0
numList = []
for i in range(testCase):
    num = int(input())
    numList.append(num)

while True:
    maxNum = 0
    index = 0
    for i in range(1, testCase, 1):
        if maxNum < numList[i]:
            maxNum = numList[i]
            index = i
    if maxNum >= numList[0]:
        numList[index] -= 1
        numList[0] += 1
        count += 1
    else:
        break

print(count)
