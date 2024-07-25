def solution(my_string):
    answer = 0
    temp = 0
    for item in my_string:
        if item.isdigit():
            temp = temp * 10 + int(item)
        else:
            answer += temp
            temp = 0
    return answer + temp


# Test Cases
print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))


"""
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())
    
    
와 대박이네
"""
