def solution(arr, divisor):
    answer = [item for item in arr if item % divisor == 0]
    return sorted(answer) if len(answer) > 0 else [-1]


# Test Cases
print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))


"""
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]


오잉
"""
