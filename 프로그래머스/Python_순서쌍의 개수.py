def solution(n):
    answer = 0
    for i in range(1, n+1):
        if not (n % i):
            answer += 1
    return answer


# Test Cases
print(solution(20))
print(solution(100))


"""
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
    
filter도 있네
"""
