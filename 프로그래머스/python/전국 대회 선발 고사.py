def solution(rank, attendance):
    answer = 0
    temp_list = []
    check_list = []
    first = 0
    second = 0
    third = 0
    for i in range(len(rank)):
        temp = rank[i] * attendance[i]
        temp_list.append(temp)
        check_list.append(temp)

    check_list.sort(reverse=True)
    while True:
        temp = check_list.pop()
        if temp == 0:
            pass
        else:
            check_list.append(temp)
            break
    check_list.sort(reverse=False)
    # print(check_list)

    for i in range(len(rank)):
        if check_list[0] == rank[i]:
            first = i
            break
    for i in range(len(rank)):
        if check_list[1] == rank[i]:
            second = i
            break
    for i in range(len(rank)):
        if check_list[2] == rank[i]:
            third = i
            break

    answer = first * 10000 + second * 100 + third

    return answer


# 테스트 케이스
print(solution([3, 7, 2, 5, 4, 6, 1], [
      False, True, True, True, True, False, False]))
print(solution([1, 2, 3], [True, True, True]))
print(solution([6, 1, 5, 2, 3, 4], [True, False, True, False, False, True]))


"""
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]
    
    
???? 이게 머지
"""
