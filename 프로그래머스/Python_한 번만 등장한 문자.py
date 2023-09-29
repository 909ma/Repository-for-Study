def solution(s):
    s = sorted(s)
    answer = ''
    for item in s:
        if item not in answer and s.count(item) == 1:
            answer += item
    return answer


# Test Cases
print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))


"""
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer
    
    
이렇게 할 껄 그랬나
"""
