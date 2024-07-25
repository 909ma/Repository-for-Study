def solution(arr1, arr2):
    return [[x + y for x, y in zip(a, b)] for a, b in zip(arr1, arr2)]


# Test Cases
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))