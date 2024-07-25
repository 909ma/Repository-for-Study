# 유클리드 호제법


# 최대공약수
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


# 최소공배수
def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result


from collections import deque

answer = True
FirstText = input()
SecondText = input()

FirstSize = len(FirstText)
SecondSize = len(SecondText)

FirstQueue = deque(FirstText)
SecondQueue = deque(SecondText)

# print(FirstQueue)
# print(SecondQueue)
loop = LCM(FirstSize, SecondSize)

for _ in range(loop):
    temp1 = FirstQueue.pop()
    temp2 = SecondQueue.pop()
    # print("=" * 50)
    # print(f"temp1: {temp1}, temp2: {temp2}")
    # print(f"FirstText: {FirstText}\nSecondText: {SecondText}")
    if temp1 == temp2:
        FirstQueue.insert(0, temp1)
        SecondQueue.insert(0, temp2)
    else:
        answer = False
        break

# print("=" * 50)
# print(answer)

if answer:
    print("1")
else:
    print("0")
