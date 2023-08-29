NumList = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

FirstName = input()
SecondName = input()
Sum = []

for i in range(len(FirstName)):
    Sum.append(NumList[ord(FirstName[i]) - 65])
    Sum.append(NumList[ord(SecondName[i]) - 65])

while len(Sum) > 2:
    temp3 = -1
    Temp = []

    while len(Sum) > 0:
        if temp3 == -1:
            temp1 = Sum.pop(0)
        else:
            temp1 = temp3
        temp2 = Sum.pop(0)
        SumTemp = (temp1 + temp2) % 10
        Temp.append(SumTemp)
        temp3 = temp2
        # print(f"temp1: {temp1}, temp2: {temp2}, SumTemp: {SumTemp}, Sum: {Sum}, Temp: {Temp}\n")
    Sum = Temp

print(f"{Sum.pop(0)}{Sum.pop(0)}")
