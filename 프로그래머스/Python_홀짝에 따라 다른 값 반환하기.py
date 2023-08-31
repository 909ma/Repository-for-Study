def solution(n):
    answer = 0
    for i in range(2 - (n % 2), n + 1, 2):
        answer += i ** (2 - (n % 2))
    return answer


print(solution(7))
print(solution(10))
