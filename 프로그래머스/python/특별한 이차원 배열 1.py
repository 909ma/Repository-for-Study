import numpy


def solution(n):
    answer = numpy.eye(n).tolist()
    return answer


"""
def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer
    
    
이렇게 풀 뻔 했는데 다행인가?
"""
"""
def solution(arr, intervals):
    answer = []
    for item in intervals:
        a, b = item
        temp = arr[a:b]
        answer.append(temp)
    return answer
    
    
입력값 〉	[1, 2, 3, 4, 5], [[1, 3], [0, 4]]
기댓값 〉	[2, 3, 4, 1, 2, 3, 4, 5]
실행 결과 〉	실행한 결괏값 [[2,3],[1,2,3,4]]이 기댓값 [2,3,4,1,2,3,4,5]과 다릅니다.

여기서 영감을 얻어서 다음에는 다르게 풀어보자
"""
