def solution(hp):
    answer = hp // 5
    hp = hp % 5
    answer += hp // 3
    hp = hp % 3
    answer += hp
    return answer


# Test Cases
print(solution(23))
print(solution(24))
print(solution(999))


"""
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer
    
    
깔끔하네
"""
