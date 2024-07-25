def solution(s):
    return ''.join(sorted([item for item in s], reverse=True))


# Test Cases
print(solution("Zbcdefg"))


"""
def solution(s):
    return ''.join(sorted(s, reverse=True))
    
    
그냥 해도 되네...
"""
