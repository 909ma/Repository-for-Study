def solution(x):
    return x % (sum([int(i) for i in str(x)])) == 0


# Test Cases
print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))
