line = input()
i = 1
while i <= len(line):
    if (i % 10 == 0) & (i != 0):
        print(line[i-1])
    else:
        print(line[i-1], end="")
    i += 1
