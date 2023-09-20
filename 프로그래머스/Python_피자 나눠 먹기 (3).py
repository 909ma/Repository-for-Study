def solution(slice, n):
    answer = (n + slice - 1) // slice
    return answer


# Test Cases
print(solution(7, 10))
print(solution(4, 12))
