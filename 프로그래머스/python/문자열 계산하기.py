def solution(my_string):
    return eval(my_string.replace(" ", ""))


# Test Cases
print(solution("3 + 4"))


"""
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
    
    
풀이가 대단하다
"""
"""
solution = eval


이렇게까지 줄여진다고...
"""
