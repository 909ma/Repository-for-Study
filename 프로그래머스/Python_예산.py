def solution(d, budget):
    d = sorted(d)
    sum_num = 0
    for i in range(len(d)):
        sum_num += d[i]
        if sum_num > budget:
            return i
    return len(d)


# Test Cases
print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))


"""
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
    
    
헐ㅋ
"""
