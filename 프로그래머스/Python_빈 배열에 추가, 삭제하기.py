def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        temp = arr[i]
        if flag[i]:
            for _ in range(temp * 2):
                answer.append(temp)
        else:
            for _ in range(temp):
                del answer[-1:]
    return answer


print(solution([3, 2, 4, 1, 3], [True, False, True, False, False]))


"""
def solution(arr, flag):
    X = []
    for i, f in enumerate(flag):
        if f:
            X += [arr[i]] * (arr[i]*2)
        else:
            for _ in range(arr[i]):
                X.pop()
    return X
    
    
리스트는 연산자가 된다를 배웠다
"""
