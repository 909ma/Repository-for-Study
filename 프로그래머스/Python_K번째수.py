def solution(array, commands):
    answer = []
    for item in commands:
        temp = array[item[0] - 1:item[1]]
        temp.sort()
        answer.append(temp[item[2] - 1])
    return answer


# Test Cases
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    
    
깔끔하다
"""
