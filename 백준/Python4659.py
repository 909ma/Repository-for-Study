while True:
    check1 = False  # 조건1
    check2 = True  # 조건2
    check3 = True  # 조건3
    VowelsCount = 0
    ConsonantsCount = 0
    inputLine = input()
    if inputLine == 'end':
        break
    length = len(inputLine)

    for i in range(length):  # 수정: range 함수의 범위 지정 방식 변경

        # 조건1
        if inputLine[i] in ['a', 'e', 'i', 'o', 'u']:
            check1 = True

        # 조건2
        if inputLine[i] in ['a', 'e', 'i', 'o', 'u']:
            VowelsCount += 1
            ConsonantsCount = 0
        else:
            ConsonantsCount += 1
            VowelsCount = 0

        if VowelsCount == 3 or ConsonantsCount == 3:
            check2 = False
            break

        # 조건3
        if i > 0 and inputLine[i] == inputLine[i - 1]:
            if inputLine[i] not in ['e', 'o']:
                check3 = False
                break

    print("<", end="")
    print(inputLine + "> is ", end="")  # 수정: 출력 형식 수정
    if check1 and check2 and check3:  # 수정: 논리 연산자 사용 방식 변경
        print("acceptable.")
    else:
        print("not acceptable.")
