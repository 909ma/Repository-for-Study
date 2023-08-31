def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) == sum(arr2):
            return 0
        else:
            return -1
    else:
        return -1


print(solution([49, 13], [70, 11, 2]))  # -1
print(solution([100, 17, 84, 1], [55, 12, 65, 36]))  # 1
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))  # 0

"""
def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))
    
잘하네
"""
