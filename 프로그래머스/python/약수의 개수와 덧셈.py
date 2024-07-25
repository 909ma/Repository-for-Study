def divisor(n):
    count = 1
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            count += 1
    return count


def solution(left, right):
    return sum([item if divisor(item) % 2 == 0 else -item for item in range(left, right + 1)])


# Test Cases
print(solution(13, 17))
print(solution(24, 27))


"""
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
    
    
이런 방법이?
"""
