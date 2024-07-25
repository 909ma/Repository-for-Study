def solution(n):
    temp_str = ''
    answer = 0
    digit = 1
    while n > 0:
        temp_str += str(n % 3)
        n //= 3
    for i in temp_str[::-1]:
        answer += int(i) * digit
        digit *= 3
    return answer


# Test Cases
print(solution(45))
print(solution(125))


"""
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
    
    
int()에 이런 기능이..?
"""
