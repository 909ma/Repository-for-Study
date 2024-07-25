def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        temp = []
        for j in range(i, i + n):
            temp.append(num_list[j])
        answer += [temp]
    return answer


# Test Cases
print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))


"""
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
    
    
나보다 낫네
"""
