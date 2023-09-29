def solution(my_string):
    answer = []
    [answer.append(int(i)) for i in my_string if i in "0123456789"]
    answer.sort()
    return answer


# Test Cases
print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))


"""
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
    
    
.isdigit()를 알아둬야하네
"""
