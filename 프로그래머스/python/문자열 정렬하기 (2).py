def solution(my_string):
    return ''.join(sorted(list(my_string.lower())))


# Test Cases
print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))


"""
def solution(my_string):
    return ''.join(sorted(my_string.lower()))
    
    
list() 안 써도 되구나
"""
