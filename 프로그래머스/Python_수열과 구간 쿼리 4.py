def solution(arr, queries):
    answer = []
    for item in queries:
        s, e, k = item
        for i in range(s, e + 1):
            if i % k:
                pass
            else:
                arr[i] += 1
    return arr


print(solution([0, 1, 2, 4, 3], [[0, 4, 1],[0, 3, 2],[0, 3, 3]]))


"""
def solution(arr, queries):
    for q in queries:
        for i in range((q[0] + q[2] - 1) // q[2] * q[2], q[1] + 1, q[2]):
            arr[i] += 1

    return arr


자세히 보진 않았는데 가장 괜찮은 듯
"""
