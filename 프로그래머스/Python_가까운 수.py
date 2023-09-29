def solution(array, n):
    answer = 0
    array.sort()
    check_list = [0] * len(array)
    for i in range(len(array)):
        check_list[i] = abs(array[i] - n)
    answer = array[check_list.index(min(check_list))]
    return answer


# Test Cases
print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))

"""
가까운 수 - Pyhon

solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]


이런 풀이가?
"""
