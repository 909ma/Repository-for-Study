def solution(sides):
    answer = 0
    num1 = max(sides)
    num2 = min(sides)
    # 1: 가장 긴 변이 num1인 경우
    """
    for i in range(num1 - num2 + 1, num1):
        answer += 1
    print(answer)
    """
    answer += num2 - 1

    # 2: 나머지 한 변이 가장 긴 변인 경우
    """
    for i in range(num1, num1 + num2):
        answer += 1
    print(answer)
    """
    answer += num2

    return answer


# Test Cases
print(solution([1, 2]))
print("="*50)
print(solution([3, 6]))
print("="*50)
print(solution([11, 7]))
