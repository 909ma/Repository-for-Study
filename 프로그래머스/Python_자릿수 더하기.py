def solution(n):
    answer = 0
    for item in str(n):
        answer += int(item)
    return answer


# Test Cases
print(solution(1234))
print(solution(930211))
