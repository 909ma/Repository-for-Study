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


def solution(numer1, denom1, numer2, denom2):
    answer = []
    temp_numer = numer1 * denom2 + numer2 * denom1
    temp_denom = denom1 * denom2
    temp_GCD = GCD(temp_numer, temp_denom)
    answer = [temp_numer/temp_GCD, temp_denom/temp_GCD]
    return answer


# Test Cases
print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))

"""
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]


역시 파이썬... 없는게 없네
"""

"""
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]
    
이것도 구현이 되어있구나...
"""
