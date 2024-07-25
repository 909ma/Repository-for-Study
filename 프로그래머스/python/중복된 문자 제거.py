def solution(my_string):
    answer = ''
    for item in my_string:
        if item in answer:
            pass
        else:
            answer += item
    return answer


# Test Cases
print(solution("people"))
print(solution("We are the world"))


"""
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
    
    
set()은 생각했는데 이거는 생각못했네
"""
