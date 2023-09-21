def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        else:
            answer = 4
    else:
        if dot[1] > 0:
            answer = 2
        else:
            answer = 3
    return answer


# Test Cases
print(solution([2, 4]))
print(solution([-7, 9]))


"""
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
    
    
창의력이 대단하네
"""
