def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer
    length = len(num_list)
    if n == 1:
        for i in range(b + 1):
            answer.append(num_list[i])
    elif n == 2:
        for i in range(a, length):
            answer.append(num_list[i])
    elif n == 3:
        for i in range(a, b + 1):
            answer.append(num_list[i])
    else:
        for i in range(a, b + 1, c):
            answer.append(num_list[i])
    return answer


print(solution(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution(4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
def solution(n, slicer, num_list):
    a, b, c = slicer
    return [num_list[:b + 1], num_list[a:], num_list[a:b + 1], num_list[a:b + 1:c]][n - 1]


줄여서 잘 쓰네
"""
"""
def solution(n, slicer, num_list):
    num_dict = {num+1 : v for num, v in enumerate([
        num_list[:slicer[1]+1],
        num_list[slicer[0]:],
        num_list[slicer[0]:slicer[1]+1],
        [num_list[i] for i in list(range(slicer[0], slicer[1]+1, slicer[2]))]]
    )}

    return num_dict[n]

    

enumerate()를 진짜 써보자
"""
