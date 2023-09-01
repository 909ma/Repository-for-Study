def solution(num_list, n):
    answer = []
    size = len(num_list)
    i = 0
    while True:
        if i >= size:
            break
        answer.append(num_list[i])
        i += n
    return answer


print(solution([4, 2, 6, 1, 7, 6], 2))
print(solution([4, 2, 6, 1, 7, 6], 4))


"""
def solution(num_list, n):
    return num_list[::n]

왠지 찝찝하더라... 이게 아직 숙달이 안 되었나보네
"""
