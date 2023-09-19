def solution(n):
    answer = []
    for i in range(n + 1):
        if i % 2:
            answer.append(i)
        else:
            pass
    return answer


# Test Cases
print(solution(10))
print(solution(15))


"""
def solution(n):
    return [i for i in range(1, n+1, 2)]
    
    
쩝
"""
