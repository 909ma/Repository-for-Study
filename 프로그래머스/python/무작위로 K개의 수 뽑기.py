def solution(arr, k):
    answer = []

    for item in arr:
        if item in answer:
            pass
        elif len(answer) < k:
            answer.append(item)

    while True:
        if len(answer) < k:
            answer.append(-1)
        else:
            break

    return answer


print(solution([0, 1, 1, 2, 2, 3], 3))
print(solution([0, 1, 1, 1, 1], 4))


"""
def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))
    
    
직관적으로 잘 풀었네
"""
