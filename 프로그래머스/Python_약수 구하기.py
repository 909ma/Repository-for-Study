def solution(n):
    return list([item for item in range(1, n+1) if (item <= n/2 or item == n) and n % item == 0])


# Test Cases
print(solution(24))
print(solution(29))
