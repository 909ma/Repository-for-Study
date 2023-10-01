def solution(quiz):
    answer = []
    for item in quiz:
        a, b = item.split(" = ")
        if eval(a) == int(b):
            answer.append("O")
        else:
            answer.append("X")
    return answer


# Test Cases
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print("=" * 50)
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
print("=" * 50)


"""
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations] 
    
    
헐ㅋ
"""
