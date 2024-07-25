def solution(arr, n):
    answer = []
    size = len(arr)
    for i in range(size):
        num1 = arr[i] + ((size + i) % 2) * n
        answer.append(num1)
    return answer


print(solution([49, 12, 100, 276, 33], 27))
print(solution([444, 555, 666, 777], 100))
