def solution(num_list):
    answer = -1
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
    return answer


print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))


"""
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i]<0:return i
    return -1

깔끔하네
"""
