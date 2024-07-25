def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
    return ans


# Test Cases
print(solution(5) == 2)
print(solution(6) == 2)
print(solution(5000) == 5)


"""
def solution(n):
    return bin(n).count('1')
    
    
2를 곱하거나 나누거나 비트시프트인걸 기억하자...
정말 멋있네
"""
