def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1
    return answer


# Test Cases
print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))
