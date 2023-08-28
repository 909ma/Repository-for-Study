testCase = int(input())
setNum = [0] * 21
num = 0
for _ in range(testCase):
    line = input().split()
    if line[0] == 'all' or line[0] == 'empty':
        oper = line[0]
    else:
        oper = line[0]
        num = int(line[1])

    if oper == 'add':
        setNum[num] = 1
    elif oper == 'remove':
        setNum[num] = 0
    elif oper == 'check':
        print(setNum[num])
    elif oper == 'toggle':
        setNum[num] = 1 - setNum[num]
    elif oper == 'all':
        setNum = [1] * 21
    elif oper == 'empty':
        setNum = [0] * 21
