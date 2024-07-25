def solution(A, B):
    return sum([a*b for a, b in zip(sorted(A), sorted(B, reverse=True))])


# Test Cases
print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))


"""
import numpy as np

def solution(A, B):
    answer = float('inf')

    A_list = []
    B_list = []
    for i in range(len(A)):
        A_list.append(A[i - len(A):] + A[:i])
    for i in range(len(B)):    
        B_list.append(B[i - len(B):] + B[:i])

    A_array = np.array(A_list)
    B_array = np.array(B_list)
    print(A_array)
    print(B_array)
    
    for item in np.dot(A_array, B_array).tolist():
        for check in item:
            if answer > check:
                answer = check
    return answer

# Test Cases
print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))



틀린 풀이라는데... 생각해보자
"""
