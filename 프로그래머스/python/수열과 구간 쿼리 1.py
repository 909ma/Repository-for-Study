def solution(arr, queries):
    for item in queries:
        s, e = item
        for i in range(s, e+1):
            arr[i] += 1
    return arr


print(solution([0, 1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]]))
