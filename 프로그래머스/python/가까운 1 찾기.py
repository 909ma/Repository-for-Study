def solution(arr, idx):
    answer = -1
    for i in range(len(arr)):
        if i < idx:
            pass
        else:
            if arr[i] == 1:
                answer = i
                return answer
    return answer


"""
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer
    
    
.index(찾는 값, 시작 위치) : 하나 배웠다
"""
