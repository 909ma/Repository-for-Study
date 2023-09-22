def solution(numbers, k):
    size = len(numbers)
    i = 0
    for _ in range(k - 1):
        i += 2
        if i >= size:
            i -= size
    answer = numbers[i]
    return answer


# Test Cases
print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))
