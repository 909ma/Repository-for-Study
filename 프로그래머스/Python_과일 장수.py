def solution(k, m, score):
    answer = 0
    score.sort()
    while True:
        if len(score) >= m:
            answer += score[-m] * m
            for _ in range(m):
                score.pop()
        else:
            break    
    return answer


"""
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m


잘 풀었네
"""
