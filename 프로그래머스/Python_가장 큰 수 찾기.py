def solution(array):
    num1 = max(array)
    num2 = array.index(num1)
    return [num1, num2]


# Test Cases
print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))
