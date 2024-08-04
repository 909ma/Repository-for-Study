def cal2(str1, str2):
    result = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            result += 1
    return result


def cal(str1, str2):
    num = len(str2) - len(str1)
    result = 50
    for i in range(num + 1):
        temp = cal2(str1, str2[i:i+len(str1)])
        result = min(result, temp)
        if result == 0:
            return 0
    return result


str1, str2 = input().split(' ')
num = len(str2) - len(str1)
print(cal(str1, str2))
