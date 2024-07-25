def solution(a, b):
    check = a % 2 + b % 2
    if check == 2:
        answer = a**2 + b**2
    elif check:
        answer = 2 * (a + b)
    else:
        answer = abs(a - b)
    return answer


print(solution(3, 5))
print(solution(6, 1))
print(solution(2, 4))

"""
def solution(a, b):
        return a*a+b*b if a & b & 1 else (a + b) << 1 if (a | b) & 1 else abs(a - b)
        
진짜 잘했네
"""
