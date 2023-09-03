PeopleList = []

size = int(input())

for _ in range(size):
    name, state = input().split()
    if state == "enter":
        PeopleList.append(name)
    else:
        PeopleList.remove(name)

PeopleList.sort(reverse=True)
OutputText = ' '.join(PeopleList)
print(OutputText)


"""
set은 add()와 remove(), sort()를 쓰면 된다.
"""
