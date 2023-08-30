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
i=[*open(0)][1].split()
d=dict(zip(sorted({*i},key=int),range(5**9)))
print(*[d[x]for x in i])

와 이게 머야
"""
