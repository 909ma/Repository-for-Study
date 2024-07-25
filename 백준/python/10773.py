stack = []
testCase = int(input())

for _ in range(testCase):
    num = int(input())
    if num == 0 and stack:
        stack.pop()
    else:
        stack.append(num)

result = sum(stack)
print(result)
