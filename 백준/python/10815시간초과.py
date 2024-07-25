size = int(input())
inputs = list(map(int, input().split()))

Dic = {}
for i in range(size):
    Dic[inputs[i]] = 1

size = int(input())
CheckList = list(map(int, input().split()))
answer = ""
for i in range(size):
    if CheckList[i] in Dic:
        answer += "1 "
    else:
        answer += "0 "

print(answer)
