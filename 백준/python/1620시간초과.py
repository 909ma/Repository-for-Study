import sys

line = sys.stdin.readline().split()
list1 = int(line[0])
testCase = int(line[1])
encyclopedia = []
for i in range(0, list1, 1):
    encyclopedia.append(sys.stdin.readline().rstrip())


for _ in range(testCase):
    line = sys.stdin.readline().rstrip()
    if line.isdigit():  # 숫자인 경우
        print(encyclopedia[int(line) - 1])
    else:
        index = 0
        for i in range(0, list1, 1):
            if line == encyclopedia[i]:
                index = i + 1
        print(index)
