def solution(s):
    answer = ''
    temp = 0
    for item in s:
        if item == " ":
            temp = 0
            answer += " "
        else:
            if temp % 2 == 0:
                temp += 1
                answer += item.upper()
            else:
                temp += 1
                answer += item.lower()
    return answer


# Test Cases
print(solution("try hello world"))
