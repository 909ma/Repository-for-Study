def factorial(n, m):
    num = 1
    while n >= m:
        num *= n
        n -= 1
    return num


def solution(balls, share):
    numerator = factorial(balls, 1)
    denominator = factorial(share, 1) * factorial(balls - share, 1)
    answer = numerator / denominator
    return answer


# Test Cases
print(solution(3, 2))
print(solution(5, 3))


"""
import math


def solution(balls, share):
    return math.comb(balls, share)
    

있을 거 같더라
"""
