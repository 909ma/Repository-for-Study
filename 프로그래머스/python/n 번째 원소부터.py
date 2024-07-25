def solution(num_list, n):
    answer = []
    i = 1
    for item in num_list:
        if i < n:
            pass
        else:
            answer.append(item)
        i += 1
    return answer


print(solution([2, 1, 6], 3))
print(solution([5, 2, 1, 7, 5], 2))


"""
def solution(num_list, n):
    return num_list[n-1:]

이런 방법을 두고...
"""
