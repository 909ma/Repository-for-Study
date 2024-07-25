def solution(absolutes, signs):
    return sum([a if b else -a for a, b in zip(absolutes, signs)])


# Test Cases
print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))
