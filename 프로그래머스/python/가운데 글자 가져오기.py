def solution(s):
    size = len(s)
    return s[size//2:size//2 + 1] if size % 2 == 1 else s[size//2 - 1:size//2 + 1]


# Test Cases
print(solution("abcde"))
print(solution("qwer"))


"""
solution = lambda s: s[(len(s) - 1) // 2 : len(s) // 2 + 1]


헐ㅋ
"""
