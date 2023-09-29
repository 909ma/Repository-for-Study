def solution(n):
    answer = 2
    check = 1
    while check**2 <= n:
        if check**2 == n:
            answer = 1
            break
        else:
            check += 1
    return answer


# Test Cases
print(solution(144))
print(solution(976))


"""
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
    
    
진짜 공부를 너무 안 했나
"""
