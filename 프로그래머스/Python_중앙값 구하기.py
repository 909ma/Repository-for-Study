def solution(array):
    mid = len(array) // 2
    array.sort()
    answer = array[mid]
    return answer


# Test Cases
print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))
