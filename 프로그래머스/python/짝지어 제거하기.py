def solution(s):
    stack = [' ']
    for right in s:
        left = stack.pop()
        if left == right:
            pass
        else:
            stack.append(left)
            stack.append(right)
    return int(len(stack) == 1)


# Test Cases
print(solution("baabaa"))
print(solution("cdcd"))


"""
def solution(s):
    temp = ""
    while temp != s:
        temp = s
        s = s.replace("aa", "")
        s = s.replace("bb", "")
        s = s.replace("cc", "")
        s = s.replace("dd", "")
        s = s.replace("ee", "")
        s = s.replace("ff", "")
        s = s.replace("gg", "")
        s = s.replace("hh", "")
        s = s.replace("ii", "")
        s = s.replace("jj", "")
        s = s.replace("kk", "")
        s = s.replace("ll", "")
        s = s.replace("mm", "")
        s = s.replace("nn", "")
        s = s.replace("oo", "")
        s = s.replace("pp", "")
        s = s.replace("qq", "")
        s = s.replace("rr", "")
        s = s.replace("ss", "")
        s = s.replace("tt", "")
        s = s.replace("uu", "")
        s = s.replace("vv", "")
        s = s.replace("ww", "")
        s = s.replace("xx", "")
        s = s.replace("yy", "")
        s = s.replace("zz", "")
    return int(len(s) == 0)


# Test Cases
print(solution("baabaa"))
print(solution("cdcd"))


시간 초과 코드
"""
