def solution(arr):
    stk = []
    i = 0
    while True:
        if i == len(arr):
            break
            
        if not(len(stk)):
            stk.append(arr[i])
            i += 1
        else:
            temp = stk.pop()
            if temp < arr[i]:
                stk.append(temp)
                stk.append(arr[i])
                i += 1
            else:
                pass
    return stk


"""
def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk


내가 너무 대충 생각했나봐
"""
