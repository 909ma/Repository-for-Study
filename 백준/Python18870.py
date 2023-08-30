import copy

size = int(input())
InputList = list(map(int, input().split(" ")))

temp = copy.deepcopy(InputList)  # 깊은 복사

temp.sort()

dic = {}  # [값, 순서]
num = 0
for i in range(size):
    if temp[i] in dic:
        continue
    else:
        dic[temp[i]] = num
        num += 1
for i in range(size):
    print(dic[InputList[i]], end=" ")

"""
5
2 4 -10 4 -9
"""
