def solution(strArr):
    temp_list = []
    for _ in range(30):
        temp_list.append(0)

    for item in strArr:
        temp = len(item) - 1
        temp_list[temp] += 1

    answer = max(temp_list)
    return answer


print(solution(["a", "bc", "d", "efg", "hi"]))

"""
def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)
    
    
또 이걸 까먹었네
"""
