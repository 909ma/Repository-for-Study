def solution(n):
    count = 1
    for i in range(1, n // 2 + 1):
        sum_num = i
        add_num = i + 1
        while sum_num < n:
            sum_num += add_num
            add_num += 1
        if sum_num == n:
            count += 1
        else:
            pass
    return count


# Test Cases
print(solution(15))
