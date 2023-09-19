def solution(array):
    answer = -1
    num_list = [0 for _ in range(1001)]
    for item in array:
        num_list[item] += 1

    max_appear = max(num_list)
    for i in range(1001):
        if max_appear == num_list[i]:
            if answer == -1:
                answer = i
            else:
                answer = -1
                break
    return answer


# Test Cases
print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))


"""
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
    
    
이런 접근 방법이?
"""
"""
from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]
    

신기하네
"""
