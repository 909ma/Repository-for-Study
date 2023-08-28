arr = input()
size = len(arr)
checkReverse = True
checkException = False
index = 0
arr = list(arr)

for i in range(size):
    if checkException:
        if arr[i] == ">":
            checkException = False
    else:
        if checkReverse:
            if arr[i] == "<":
                checkException = True
            else:
                index = i
                checkReverse = False
        else:
            if arr[i] == "<":
                arr[index:i] = reversed(arr[index:i])
                checkReverse = True
                checkException = True
            elif arr[i] == " ":
                arr[index:i] = reversed(arr[index:i])
                checkReverse = True
            elif i == size - 1 and arr[i] != ">":
                arr[index:i + 1] = reversed(arr[index:i + 1])
                checkReverse = True

print(''.join(arr))
