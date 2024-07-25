def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))


# Test Cases
print(solution(118372))

"""
def solution(n):
    return int(''.join(sorted(list(str(n)), reverse = True)))


# Test Cases
print(solution(118372))


처럼도 가능하다 까먹지 말자
"""
