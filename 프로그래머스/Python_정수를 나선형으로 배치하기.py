n = 3

answer = [[0]*n]*n

up = False
down = False
left = False
right = True

count = 1
i = 0
j = 0

while True:
    if count == n**2 + 1:
        break
    elif right:
        if j < n:
            if answer[i][j] == 0:
                answer[i][j] = count
                count += 1
                j += 1
            else:
                j -= 1
                i += 1
                right = False
                down = True
        else:
            right = False
            down = True
            j -= 1
            i += 1
    elif down:
        if i < n:
            if answer[i][j] == 0:
                answer[i][j] = count
                count += 1
                i += 1
            else:
                i -= 1
                j -= 1
                down = False
                left = True
        else:
            i -= 1
            j -= 1
            down = False
            left = True
    elif left:
        if j >= 0:
            if answer[i][j] == 0:
                answer[i][j] = count
                count += 1
                j -= 1
            else:
                i -= 1
                j += 1
                left = False
                up = True
        else:
            i -= 1
            j += 1
            left = False
            up = True
    elif up:
        if i >= 0:
            if answer[i][j] == 0:
                answer[i][j] = count
                count += 1
                i -= 1
            else:
                i += 1
                j -= 1
                up = False
                right = True
        else:
            i += 1
            j -= 1
            up = False
            right = True

print(answer)
