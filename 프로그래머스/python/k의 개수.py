def solution(i, j, k):
    answer = 0
    for item in range(i, j + 1):
        answer += str(item).count(str(k))
    return answer


# Test Cases
print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10, 2))
