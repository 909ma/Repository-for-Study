import sys

testCase1 = int(sys.stdin.readline().rstrip())
for _ in range(testCase1):
    clothSet = set()
    clothList = []
    testCase2 = int(sys.stdin.readline().rstrip())
    for i in range(testCase2):
        line = sys.stdin.readline().rstrip().split()
        clothList.append(line[1])
        if line[1] in clothSet:
            pass
        else:
            clothSet.add(line[1])

    clothCount = list(clothSet)
    length = len(clothSet)
    product = 1
    for i in range(length):
        product *= (clothList.count(clothCount[i]) + 1)

    product -= 1
    print(product)
