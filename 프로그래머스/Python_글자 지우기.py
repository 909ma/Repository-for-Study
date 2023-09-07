def solution(my_string, indices):
    answer = ''
    temp = 0
    indices.sort()
    for item in indices:
        answer += my_string[temp:item]
        temp = item + 1
    answer += my_string[temp:]
    return answer


print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]))


"""
def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer
    
    
괜찮네
"""
