def solution(n):
    answer = 0
    for i in range(0, n + 1, 2):
        answer += i
    return answer


# Test Cases
print(solution(10))
print(solution(4))


"""
def solution(n):
    return 2*(n//2)*((n//2)+1)/2
    
    
등차수열의 합 공식...
"""
