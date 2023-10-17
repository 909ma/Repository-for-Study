def solution(brown, yellow):
    for i in range(1, brown + yellow + 1):
        x, y = i, (brown + yellow) / i
        if (x - 2) * (y - 2) == yellow:
            return [int(y), x]
    return 0


# Test Cases
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
