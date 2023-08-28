while True:
    try:
        lineA, lineB = input().split()
        sizeA = len(lineA)
        sizeB = len(lineB)
        check = False
        count = 0
        for i in range(sizeB):
            if lineB[i] == lineA[count]:
                count += 1
            if count == sizeA:
                check = True
                break

        if check:
            print("Yes")
        else:
            print("No")
    except:
        break
