inputLine = []
for i in range(8):
    inputLine.append(input())

count = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if inputLine[i][j] == 'F':
                count += 1
print(count)
