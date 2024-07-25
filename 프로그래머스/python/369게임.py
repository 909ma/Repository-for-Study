def solution(order):
    answer = str(order).count("3")
    answer += str(order).count("6")
    answer += str(order).count("9")
    return answer


# Test Cases
print(solution(3))
print(solution(29423))


"""
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
    
    
신기하네
"""
