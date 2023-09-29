def solution(my_string):
    answer = ''
    for item in my_string:
        if item.isupper():
            answer += item.lower()
        else:
            answer += item.upper()
    return answer


# Test Cases
print(solution("cccCCC"))
print(solution("abCdEfghIJ"))


"""
def solution(my_string):
    return my_string.swapcase()
    
    
헐ㅋ
"""
