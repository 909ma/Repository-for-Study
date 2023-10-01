def solution(num, total):
    answer = []
    if num % 2:
        start = total // num - (num - 1) // 2
        end = total // num + (num - 1) // 2
        for i in range(start, end + 1):
            answer.append(i)
    else:
        start = total // num - num // 2 + 1
        end = total // num + num // 2
        for i in range(start, end + 1):
            answer.append(i)
    return answer


# Test Cases
print(solution(3, 12))
print("=" * 50)
print(solution(5, 15))
print("=" * 50)
print(solution(4, 14))
print("=" * 50)
print(solution(5, 5))
print("=" * 50)


"""
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]

    
내 풀이를 좀 더 간소화할 수 있었는데 ㄲㅂ
"""
