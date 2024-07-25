def solution(a, b, n):
    answer = 0
    while n >= a:
        temp = n // a * b
        answer += temp
        n = n % a + temp
    return answer


# Test Cases
print(solution(2, 1, 20))
print(solution(3, 1, 20))


"""
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b


오늘은 머리가 덜 돌아가는군
"""
