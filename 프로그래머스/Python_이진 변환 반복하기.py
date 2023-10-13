def solution(s):
    zero = 0
    count = 0
    while s != '1':
        zero += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s)))[2:]
        count += 1
    return [count, zero]


# Test Cases
print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))


"""
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]


발상의 전환?
"""
