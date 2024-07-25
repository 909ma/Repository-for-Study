def solution(X, Y):
    X_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Y_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(0, 10):
        X_list[i] = X.count(str(i))
        Y_list[i] = Y.count(str(i))
        
    answer = ''
    for i in range(9, -1, -1):
        if i != 0 or len(answer) != 0:
            while X_list[i] != 0 and Y_list[i] != 0:
                answer += f"{i}"
                X_list[i] -= 1
                Y_list[i] -= 1
        elif i == 0 and (X_list[i] != 0 and Y_list[i] != 0):
            answer = '0'
        else:
            answer = '-1'
    return answer
  
"""
def solution(X, Y):
    X_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Y_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(0, 10):
        X_list[i] = X.count(str(i))
        Y_list[i] = Y.count(str(i))
        
    answer = ''
    for i in range(9, -1, -1):
        while X_list[i] != 0 and Y_list[i] != 0:
            answer += f"{i}"
            X_list[i] -= 1
            Y_list[i] -= 1
            
    return str(int(answer)) if answer != '' else "-1"


시간초과 뜨네
"""

"""
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer


개잘했네
"""
