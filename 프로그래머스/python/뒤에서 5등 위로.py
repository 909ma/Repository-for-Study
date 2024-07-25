def solution(num_list):
    num_list.sort()
    answer = num_list[5:]
    return answer

print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))
