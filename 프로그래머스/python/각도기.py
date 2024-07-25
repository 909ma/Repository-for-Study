def solution(angle):
    if angle == 180:
        answer = 4
    elif angle > 90:
        answer = 3
    elif angle == 90:
        answer = 2
    else:
        answer = 1
    return answer


# Test Cases
print(solution(70))
print(solution(91))
print(solution(180))


"""
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
    
    
수학적인 계산을 자꾸 빼먹네
"""
