def solution(n, numlist):
    answer = []
    [answer.append(item) for item in numlist if item % n == 0]
    return answer


# Test Cases
print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution(5, [1, 9, 3, 10, 13, 5]))
print(solution(12, [2, 100, 120, 600, 12, 12]))


"""
def solution(n, numlist):
    answer = [i for i in numlist if i%n==0]
    return answer
    
    
나보다 낫다
"""
"""
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))
    
    
헐
"""
