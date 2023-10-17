def solution(numbers):
    temp_set = set()
    for i, item in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            temp_set.add(item + numbers[j])
    return sorted(list(temp_set))


# Test Cases
print(solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7])
print(solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12])
