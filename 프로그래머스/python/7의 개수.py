def solution(array):
    return sum([str(item).count("7") for item in array])


# Test Cases
print(solution([7, 77, 17]))
print(solution([10, 29]))


"""
def solution(array):
    return str(array).count('7')
    
    
헐ㅋ
"""
