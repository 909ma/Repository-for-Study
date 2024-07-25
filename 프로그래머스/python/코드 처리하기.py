def solution(code):
    answer = ''
    check = True
    for i in range(len(code)):
        char = code[i]
        if char in ["0", "1"]:
            check = not(check)
            continue

        if check:
            if not(i % 2):
                answer += code[i]
        else:
            if i % 2:
                answer += code[i]
    if len(answer) == 0:
        answer = "EMPTY"
    return answer

print(solution("abc1abc1abc"))

'''
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"

신기하네
'''
