def solution(numbers):
    return sum(range(0, 10)) - sum(numbers)


# Test Cases
print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))
