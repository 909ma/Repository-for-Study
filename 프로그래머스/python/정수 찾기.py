def solution(num_list, n):
    answer = int(n in num_list)
    return answer

print(solution([1, 2, 3, 4, 5], 3))
print(solution([15, 98, 23, 2, 15], 20))
