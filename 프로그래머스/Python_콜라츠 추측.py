def solution(n):
    answer = 0
    for _ in range(500):
        if n == 1:
            return answer
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        answer += 1
    return -1


# Test Cases
print(solution(6))
print(solution(16))
print(solution(626331))
