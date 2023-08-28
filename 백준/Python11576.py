A, B = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))

deci = 0
nowNum = 1
for i in range(len(num)-1, -1, -1):
    deci += num[i] * nowNum
    nowNum *= A

answer = []
while deci > 0:
    reminder = deci % B
    deci = deci//B
    answer.append(reminder)

for i in range(len(answer)-1,-1,-1):
    print(answer[i], end=" ")