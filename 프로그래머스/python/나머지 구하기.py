def solution(num1, num2):
    answer = num1 % num2
    return answer


# Test Cases
print(solution(3, 2))
print(solution(10, 5))


"""
def solution(num1, num2):
    return divmod(num1, num2)[1]
    
    
이런 것도 있구나
"""
