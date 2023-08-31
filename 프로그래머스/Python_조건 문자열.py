def solution(ineq, eq, n, m):
    check = ord(ineq) + ord(eq)
    if check == 121:
        answer = int(n <= m)
    elif check == 93:
        answer = int(n < m)
    elif check == 123:
        answer = int(n >= m)
    else:
        answer = int(n > m)
    return answer


print(solution("<", "=", 20, 50))
print(solution(">", "!", 41, 78))
"""
print(ord("<") + ord("="))  # 121
print(ord("<") + ord("!"))  # 93
print(ord(">") + ord("="))  # 123
print(ord(">") + ord("!"))  # 95
"""
"""
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

eval() 함수 배웠네    
"""
