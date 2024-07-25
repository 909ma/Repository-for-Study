answer = input()
answerLength = len(answer)
testCase = int(input())
countAnswer = 0

for _ in range(testCase):
    inputLine = input()
    length = len(inputLine)
    inputLine += inputLine
    check = False
    count = 0
    for i in range(length):
        if inputLine[i] == answer[0]:
            if inputLine[i:i+answerLength] == answer:
                check = True
                break

    if check:
        countAnswer += 1

print(countAnswer)
