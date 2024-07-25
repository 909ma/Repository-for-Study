def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + common[1] - common[0]
    else:
        return common[-1] * (common[1] / common[0])


# Test Cases
print(solution([1, 2, 3, 4]))
print("=" * 50)
print(solution([2, 4, 8]))
print("=" * 50)


"""
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer
    
    
아이디어가 좋네
"""
