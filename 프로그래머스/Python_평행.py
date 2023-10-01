def degree(dot, num1, num2):
    return (dot[num2][1] - dot[num1][1]) / (dot[num2][0] - dot[num1][0])


def solution(dot):
    if degree(dot, 0, 1) == degree(dot, 2, 3):
        return 1
    elif degree(dot, 0, 2) == degree(dot, 1, 3):
        return 1
    elif degree(dot, 0, 3) == degree(dot, 1, 2):
        return 1
    else:
        return 0


# Test Cases
print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print("=" * 50)
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
print("=" * 50)


"""
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0
    
    
이게 가독성이 더 좋네;
"""
