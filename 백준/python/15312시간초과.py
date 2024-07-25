NumList = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

FirstName = input()
SecondName = input()
Sum = ""

for i in range(len(FirstName)):
    Sum += str(NumList[ord(FirstName[i]) - 65])
    Sum += str(NumList[ord(SecondName[i]) - 65])

while len(Sum) > 2:
    temp = ""
    for i in range(len(Sum) - 1):
        num1 = int(Sum[i])
        num2 = int(Sum[i + 1])
        num3 = str(num1 + num2)
        temp += num3[-1]
    Sum = temp

print(Sum)
