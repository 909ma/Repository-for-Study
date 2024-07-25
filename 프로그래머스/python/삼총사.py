def solution(number):
    answer = 0
    number.sort()
    for i in range(len(number) - 2):
        for j in range(i + 1, len(number) - 1):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer


# Test Cases
print(solution([-2, 3, 0, -3, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))


"""
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt
    
    
헐ㅋ;
"""
