from collections import deque


def solution(my_string, is_suffix):
    size = len(is_suffix)
    answer = True
    if size > len(my_string):
        answer = False
    else:
        deque1 = deque(my_string)
        deque2 = deque(is_suffix)
        for i in range(size):
            if deque1.pop() == deque2.pop():
                continue
            else:
                answer = False
    return int(answer)


print(solution("banana", "ana"))
print(solution("banana", "nan"))
print(solution("banana", "wxyz"))
print(solution("banana", "abanana"))

"""
def solution(m, s):
    if m[-len(s):]==s: return 1
    return 0
헐ㅋ
"""
