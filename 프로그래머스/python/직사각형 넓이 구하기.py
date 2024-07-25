def solution(dots):
    dot_x = [dots[0][0], dots[1][0], dots[2][0], dots[3][0]]
    dot_y = [dots[0][1], dots[1][1], dots[2][1], dots[3][1]]
    return (max(dot_x) - min(dot_x))*(max(dot_y) - min(dot_y))


# Test Cases
print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print("="*50)
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))
print("="*50)


"""
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
    
    
이렇게 하면 되네
"""
