def solution(arr, intervals):
    answer = []
    for item in intervals:
        a, b = item
        temp = arr[a : b + 1]
        for item2 in temp:
            answer.append(item2)
    return answer


"""
def solution(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1] + arr[s2:e2+1]
    
    
헐ㅋ list는 + 연산자가 되구나
"""
