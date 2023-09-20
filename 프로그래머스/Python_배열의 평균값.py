def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer


# Test Cases
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))


"""
import numpy as np
def solution(numbers):
    return np.mean(numbers)
    
    
numpy에 대해 자세히 알아봐야겠구만...
math에 avg가 없어서 그냥 단순하게 풀었네
"""
