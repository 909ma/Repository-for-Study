def solution(numbers, n):
    answer = 0
    for item in numbers:
        if answer <= n:
            answer += item
    return answer


print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))


"""
def solution(numbers, n):
    return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)


next(), iter()
https://dojang.io/mod/page/view.php?id=2408
어렵다 어려워
"""
