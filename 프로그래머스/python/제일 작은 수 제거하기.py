def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]


# Test Cases
print(solution([4, 3, 2, 1]))
print(solution([10]))


"""
def solution(arr):
    return [item for item in arr if item != min(arr)] or [-1]


# Test Cases
print(solution([4, 3, 2, 1]))
print(solution([10]))


이거 시간초과임
"""
