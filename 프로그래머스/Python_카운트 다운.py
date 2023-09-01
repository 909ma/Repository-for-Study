def solution(start, end_num):
    answer = []
    for i in range(start, end_num - 1, -1):
        answer.append(i)
    return answer


print(solution(10, 3))

"""
def solution(start, end):
    return list(range(start,end-1,-1))

이렇게 할껄;
"""
