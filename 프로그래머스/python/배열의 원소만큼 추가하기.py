def solution(arr):
    answer = []
    for item in arr:
        for i in range(item):
            answer.append(item)
    return answer


print(solution([5, 1, 4]))
print(solution([6, 6]))
print(solution([1]))
