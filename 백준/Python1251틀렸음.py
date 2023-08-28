InputText = input()
StrSize = len(InputText)
FirstChar = "z"
FirstPosition = 0
SecondChar = "z"
SecondPosition = 0

for i in range(StrSize):
    if InputText[i : i + 1] < FirstChar:
        FirstChar = InputText[i : i + 1]
        FirstPosition = i
    if InputText[i : i + 1] < SecondChar and i != FirstPosition:
        SecondChar = InputText[i : i + 1]
        SecondPosition = i

FirstStr = ""
SecondStr = ""
ThirdStr = ""

if FirstPosition < SecondPosition:
    FirstStr = InputText[0 : FirstPosition + 1]
    SecondStr = InputText[FirstPosition + 1 : SecondPosition + 1]
    ThirdStr = InputText[SecondPosition + 1 :]
    print(FirstStr[::-1], end="")
    print(SecondStr[::-1], end="")
    print(ThirdStr[::-1], end="")


elif FirstPosition > SecondPosition:
    FirstStr = InputText[0 : SecondPosition + 1]
    SecondStr = InputText[SecondPosition + 1 : FirstPosition + 1]
    ThirdStr = InputText[FirstPosition + 1 :]
    print(SecondStr[::-1], end="")
    print(FirstStr[::-1], end="")
    print(ThirdStr[::-1], end="")
