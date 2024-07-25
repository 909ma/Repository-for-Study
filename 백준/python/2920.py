numList = list(map(int, input().split(" ")))

numListAsc = sorted(numList, reverse=False)
numListDes = sorted(numList, reverse=True)
if numList == numListAsc:
    print("ascending")
elif numList == numListDes:
    print("descending")
else:
    print("mixed")
