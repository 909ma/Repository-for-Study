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
"""
모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.

그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.

계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.
"""
