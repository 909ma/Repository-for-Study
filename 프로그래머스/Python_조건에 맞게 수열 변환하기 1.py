def solution(arr):
    answer = []
    for item in arr:
        if item >= 50 and item % 2 == 0:
            item = int(item / 2)
            answer.append(item)
        elif item < 50 and item % 2 == 1:
            item = int(item * 2)
            answer.append(item)
        else:
            answer.append(item)
    return answer


print(solution([1, 2, 3, 100, 99, 98]))
