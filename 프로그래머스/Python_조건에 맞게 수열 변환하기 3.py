def solution(arr, k):
    answer = []
    check = k % 2
    for item in arr:
        answer.append((item * k) * check + (item + k) * (1 - check))
    return answer


print(solution([1, 2, 3, 100, 99, 98], 3))
print(solution([1, 2, 3, 100, 99, 98], 2))


"""
def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))

    return list(map(lambda x: x + k, arr))
    
map이랑 lambda를 잘 쓰니 이렇게도 되네
"""
