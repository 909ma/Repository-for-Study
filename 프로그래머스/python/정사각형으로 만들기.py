def solution(arr):
    size_i = len(arr)
    size_j = len(arr[0])
    max_size = max(size_i, size_j)
    new_arr = [[0] * max_size for _ in range(max_size)]
    for i in range(size_i):
        for j in range(size_j):
            new_arr[i][j] = arr[i][j]

    return new_arr


# 테스트 케이스
print(solution([[572, 22, 37], [287, 726, 384],
      [85, 137, 292], [487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
print(solution([[1, 2], [3, 4]]))
