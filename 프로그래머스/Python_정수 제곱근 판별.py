def solution(n):
    i = 1
    while i**2 <= n:
        if i**2 == n:
            return (i + 1)**2
        else:
            i += 1
    return -1


# Test Cases
print(solution(121))
print(solution(3))


"""
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
    
    
이게 맞지
"""
