def solution(num_list):
    even = 0
    odd = 0
    for item in num_list:
        if item % 2:
            odd += 1
        else:
            even += 1
    answer = [even, odd]
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))


"""
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
    
    
리스트니까 이게 되지 맞아...
"""
