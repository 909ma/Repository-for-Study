InputText = input()
Search = input()
size = len(Search)
count = 0
i = 0
while i <= len(InputText) - size:
    if InputText[i : i + size] == Search:
        count += 1
        i += size
    else:
        i += 1

print(count)

"""
print(input().count(input()))
으로 간단하게 가능하네
"""
