def solution(n):
    answer = 0
    sieve = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False
    answer = sum(sieve)
    return answer


"""
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


에라토스테네스의 체
"""
