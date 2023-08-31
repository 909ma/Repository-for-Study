def solution(number, n, m):
    answer = int(not (number % n + number % m))
    return answer
