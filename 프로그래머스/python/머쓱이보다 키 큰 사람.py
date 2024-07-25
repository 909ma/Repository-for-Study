def solution(array, height):
    return sum([1 for item in array if item > height])


# Test Cases
print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))


"""
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
    
    
신기한 풀이 발견했다
"""
