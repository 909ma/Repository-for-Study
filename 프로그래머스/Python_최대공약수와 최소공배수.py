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


def solution(n, m):
    return [GCD(n, m), LCM(n, m)]


# Test Cases
print(solution(3, 12))
print(solution(2, 5))


"""
def solution(n, m):
    def gcd(a, b): return b if not a % b else gcd(b, a % b)
    def lcm(a, b): return a*b//gcd(a, b)
    return [gcd(n, m), lcm(n, m)]


대단하네
"""
