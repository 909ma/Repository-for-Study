def solution(numbers):
    answer = []
    for item in numbers:
        answer.append(2 * item)
    return answer


# Test Cases
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))
