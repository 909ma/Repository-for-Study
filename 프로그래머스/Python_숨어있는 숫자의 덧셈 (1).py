def solution(my_string):
    answer = 0
    for item in my_string:
        if item.isdigit():
            answer += int(item)
    return answer


# Test Cases
print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))


"""
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
    
    
sum() 까먹었네
"""
