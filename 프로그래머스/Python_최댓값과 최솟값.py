def solution(s):
    temp = list(map(int, s.split()))
    return f'{min(temp)} {max(temp)}'


# Test Cases
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
