def solution(num_list):
    odd = ""
    even = ""
    for item in num_list:
        if item % 2:
            even += str(item)
        else:
            odd += str(item)
    answer = int(odd) + int(even)
    return answer


print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))
