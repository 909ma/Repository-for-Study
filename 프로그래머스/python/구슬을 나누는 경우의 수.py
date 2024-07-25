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
"""
def comb(n, m):
    if n == m or m == 0:
        return 1
    else:
        return comb(n - 1, m - 1) + comb(n - 1, m)

def solution(balls, share):
    return comb(balls, share)

# Test Cases
print(solution(3, 2))
print(solution(5, 3))


파스칼의 삼각형 어때?
"""
