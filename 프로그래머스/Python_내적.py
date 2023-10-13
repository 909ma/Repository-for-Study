def solution(a1, b1):
    return sum([a*b for a, b in zip(a1, b1)])


# Test Cases
print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))
