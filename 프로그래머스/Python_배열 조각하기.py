def solution(arr, query):
    for i in range(len(query)):
        if i % 2:
            arr = arr[query[i]:]
        else:
            arr = arr[:query[i]+1]
    return arr


# 테스트 케이스
print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))


"""
def solution(arr, query):
    for k, q in enumerate(query):
        if k % 2 == 0:
            arr = arr[:q + 1]
        else:
            arr = arr[q:]
    return arr
    
    
enumerate() 진짜 좀 공부해보자
"""
