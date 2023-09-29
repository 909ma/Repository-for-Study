def solution(before, after):
    return int(sorted(before) == sorted(after))


# Test Cases
print(solution("olleh", "hello"))
print(solution("allpe", "apple"))
