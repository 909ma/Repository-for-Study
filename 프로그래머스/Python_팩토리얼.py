def solution(n):
    answer = 1
    while n:
        n //= answer
        answer += 1
    return answer - 2


# Test Cases
print(solution(3628800))
print(solution(7))
print(solution(1))
