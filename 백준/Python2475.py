inputLine = input().split(" ")
A1 = int(inputLine[0])
A2 = int(inputLine[1])
A3 = int(inputLine[2])
A4 = int(inputLine[3])
A5 = int(inputLine[4])
answer = A1 ** 2 + A2 ** 2 + A3 ** 2 + A4 ** 2 + A5 ** 2
answer %= 10
print(answer)
