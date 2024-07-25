line = input()
while line != "0":
    length = len(line)
    check = True
    for i in range(0, length, 1):
        if line[i] == line[length - i - 1]:
            pass
        else:
            check = False
            break

    if check:
        print("yes")
    else:
        print("no")
    line = input()
