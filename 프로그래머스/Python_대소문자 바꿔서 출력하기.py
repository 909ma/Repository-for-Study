InputText = input()
answer = ""

for item in range(len(InputText)):
    NowChar = InputText[item]
    if "A" <= NowChar <= "Z":
        NowChar = NowChar.lower()
        answer = answer + NowChar
    elif "a" <= NowChar <= "z":
        NowChar = NowChar.upper()
        answer = answer + NowChar
    else:
        answer = answer + NowChar

print(answer)

"""
길게 쓸 필요없이
print(input().swapcase())
로 끝나네
"""
