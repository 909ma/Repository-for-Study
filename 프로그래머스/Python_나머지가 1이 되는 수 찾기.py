def solution(n):
    for i in range(1, n + 1):
        if n % i == 1:
            return i


# Test Cases
print(solution(10))
print(solution(12))
