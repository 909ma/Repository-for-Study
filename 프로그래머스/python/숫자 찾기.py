def solution(num, k):
    answer = -1
    num_str = str(num)
    if str(k) in num_str:
        answer = num_str.index(str(k)) + 1
    return answer


# Test Cases
print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))
