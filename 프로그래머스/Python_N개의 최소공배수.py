def gcd(a, b):
    return b if not a % b else gcd(b, a % b)


def lcm(a, b):
    return a*b//gcd(a, b)


def solution(arr):
    answer = 1
    for item in arr:
        answer = lcm(answer, item)
    return answer


# Test Cases
print(solution([2, 6, 8, 14]) == 168)
print(solution([1, 2, 3]) == 6)
