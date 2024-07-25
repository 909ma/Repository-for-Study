# 유클리드 호제법

# 최대공약수
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


# 최소공배수
def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result


def solution(n):
    answer = LCM(n, 6) / 6
    return answer


# Test Cases
print(solution(6))
print(solution(10))
print(solution(4))


"""
import math

def solution(n):
    return math.lcm(n, 6) / 6


# Test Cases
print(solution(6))
print(solution(10))
print(solution(4))


프로그래머스는 이게 안 된다. 그 이유는...
프로그래머스는 Python 3.8.5
math.lcm은 Python 3.9에서 추가된 함수라서
"""
