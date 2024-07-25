def solution(num_list):
    odd = 0
    even = 0

    for i in range(len(num_list)):
        if i % 2:
            even += num_list[i]
        else:
            odd += num_list[i]

    answer = max(odd, even)
    return answer


print(solution([4, 2, 6, 1, 7, 6]))
print(solution([-1, 2, 5, 6, 3]))


"""
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
    
    
이걸 또 까먹었네 아
"""
