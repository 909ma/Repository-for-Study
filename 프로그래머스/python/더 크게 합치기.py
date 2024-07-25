def solution(a, b):
    answer = 0
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    num1 = int(str1)
    num2 = int(str2)
    if num1 >= num2:
        answer = num1
    else:
        answer = num2
    return answer


"""
max(int(f"{a}{b}"), int(f"{b}{a}"))

너무 직관적으로 생각했네
"""
