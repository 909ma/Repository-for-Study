def solution(a, b):
    divisor = 2
    while divisor <= min(a, b):
        if a % divisor == 0 and b % divisor == 0:
            a //= divisor
            b //= divisor
            divisor = 2
        else:
            divisor += 1
    while b != 1:
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            return 2
    return 1


# Test Cases
print(solution(7, 20))
print("="*50)
print(solution(11, 22))
print("="*50)
print(solution(12, 21))
print("="*50)


"""
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2
    
    

이렇게 해도 되지 ㅋ
"""
