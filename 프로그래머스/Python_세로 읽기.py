def solution(my_string, m, c):
    answer = ""
    i = 0
    while True:
        if c - 1 + m * i < len(my_string):
            answer += my_string[c - 1 + m * i]
            i += 1
        else:
            break
    return answer


"""
def solution(s, m, c):
return s[c-1::m]

이런 것도 있네
슬라이싱 공부 당했다.
"""
