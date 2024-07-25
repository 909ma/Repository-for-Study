def solution(arr):
    answer = []
    start = -1
    end = -1
    size = len(arr)
    for i in range(size):
        if arr[i] == 2:
            start = i
            break
    for i in range(size - 1, -1, -1):
        if arr[i] == 2:
            end = i + 1
            break

    if start == -1:
        answer = [-1]
    else:
        answer = arr[start:end]
    return answer


print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
