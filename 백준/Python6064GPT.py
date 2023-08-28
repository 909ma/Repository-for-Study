def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())

    # x에서 시작하여 m씩 증가하는 수열을 만듦
    # 이 수열에서 y를 찾는 것이 목표
    while x <= lcm(m, n):
        if x % n == y % n:
            break
        x += m

    if x > lcm(m, n):
        print(-1)
    else:
        print(x)
