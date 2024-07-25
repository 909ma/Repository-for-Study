def solution(arr):
    answer = 0
    while True:
        temp = []
        for item in arr:
            if item >= 50 and item % 2 == 0:
                temp.append(item // 2)
            elif item < 50 and item % 2 == 1:
                temp.append(item*2 + 1)
            else:
                temp.append(item)
        if temp == arr:
            break
        else:
            arr = temp
        answer += 1
    return answer


print(solution([1, 2, 3, 100, 99, 98]))
