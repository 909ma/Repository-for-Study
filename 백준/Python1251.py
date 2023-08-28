InputText = input()
SizeStr = len(InputText)
answer = ""
TempStr = ""

for i in range(1, SizeStr - 1):
    for j in range(i + 1, SizeStr):
        TempStr = ""
        FirstStr = InputText[0:i]
        SecondStr = InputText[i:j]
        ThirdStr = InputText[j:]
        TempStr = FirstStr[::-1] + SecondStr[::-1] + ThirdStr[::-1]
        # print(f"i: {i}, j: {j}, TempStr: {TempStr}, answer: {answer}")
        if i == 1 and j == 2:
            answer = TempStr
        elif TempStr < answer:
            answer = TempStr

print(answer)
