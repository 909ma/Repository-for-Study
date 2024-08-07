num = int(input())
result = 0
for _ in range(num):
    message = input()
    if "01" in message:
        result += 1
    elif "OI" in message:
        result += 1

print(result)
