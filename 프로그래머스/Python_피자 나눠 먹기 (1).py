def solution(n):
    a, b = divmod(n, 7)
    answer = a + int(bool(b))
    return answer


# Test Cases
print(solution(7))
print(solution(1))
print(solution(15))

"""
def solution(n):
    return (n + 6) // 7
    

이렇게 할껄
"""
