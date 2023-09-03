def solution(n):
    answer = []
    answer.append(n)
    while True:
        if n == 1:
            break
            
        if n % 2:
            n = 3 * n + 1
            answer.append(n)
        else:
            n = n//2
            answer.append(n)
    return answer


"""
콜라츠 수열을 처음 보네

def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer



//= 도 되구나
일단 해볼껄
"""
