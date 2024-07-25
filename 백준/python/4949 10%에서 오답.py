from collections import deque

i = 0
InputText = []
answer = []

while True:
    InputText.append(input())
    if InputText[i][0] == ".":
        break
    i += 1

for i in range(len(InputText) - 1):
    size = len(InputText[i])
    check = True
    queue = deque()

    for j in range(size):
        char = InputText[i][j]

        if char == "[":
            queue.append("[")
        elif char == "(":
            queue.append("(")
        elif char == "]":
            if len(queue) == 0:
                check = False
                break
            else:
                char2 = queue.pop()
                if char2 == "[":
                    pass
                else:
                    check = False
                    break
        elif char == ")":
            if len(queue) == 0:
                check = False
                break
            else:
                char2 = queue.pop()
                if char2 == "(":
                    pass
                else:
                    check = False
                    break

    if check:
        answer.append("yes")
    else:
        answer.append("no")

OutputText = "\n".join(answer)
print(OutputText)
